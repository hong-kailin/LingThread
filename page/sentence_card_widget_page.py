from ui import Ui_sentence_card_widget
from PySide6.QtWidgets import QFrame, QMenu
from PySide6.QtCore import QEvent, QTimer, Qt, Signal
from database import SentenceCard
import time


class SentenceCardWidgetPage(QFrame, Ui_sentence_card_widget):
    translate_sentence_signal = Signal(str)

    def __init__(self, parent, sentence, sentence_translate_assistant=None):
        super().__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.sentence_translate_assistant = sentence_translate_assistant

        self.translate_sentence_signal.connect(self.sentence_translate_assistant.translate_sentence)
        self.sentence_translate_assistant.return_result_signal.connect(self.set_info_from_ai)
        self.translate.installEventFilter(self)
        self.translate.hide()
        self.sentence_card = SentenceCard(sentence)
        self.sentence.setText(self.sentence_card.sentence)

        self.is_expanded = False
        self.is_editing = False
        self.timer = QTimer(self)
        self.sentence.mousePressEvent = self.label_mouse_press_event
        self.sentence.mouseReleaseEvent = self.label_mouse_release_event
        self.timer.timeout.connect(self.check_long_press)

        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.show_context_menu)

    def show_context_menu(self, pos):
        menu = QMenu(self)
        delete_action = menu.addAction("删除卡片")
        delete_action.triggered.connect(self.delete_sentence_card)
        menu.exec(self.mapToGlobal(pos))

    def delete_sentence_card(self):
        self.parent.delete_sentence(self.sentence_card.sentence)

    def label_mouse_press_event(self, event):
        if event.button() == Qt.LeftButton:
            self.press_time = time.time()
            self.timer.start(100)
        super().mousePressEvent(event)

    def label_mouse_release_event(self, event):
        if event.button() == Qt.LeftButton:
            self.timer.stop()
            if time.time() - self.press_time < 2:
                self.sentence.setStyleSheet("background-color: rgb(17, 45, 78);")
        super().mouseReleaseEvent(event)

    def check_long_press(self):
        if time.time() - self.press_time >= 2:
            self.timer.stop()
            self.sentence.setStyleSheet("background-color: rgb(63, 114, 175);")
            self.translate_sentence_signal.emit(self.sentence_card.sentence)

    def translate_height_change(self):
        self.adjust_text_edit_height(self.translate)

    def adjust_text_edit_height(self, text_edit):
        if not text_edit.isVisible():
            return

        doc = text_edit.document()
        doc_height = doc.size().height()

        contents_margins = text_edit.contentsMargins()
        margins_height = contents_margins.top() + contents_margins.bottom()

        min_height = text_edit.minimumHeight()
        new_height = int(doc_height + margins_height + 10)
        new_height = max(min_height, new_height)

        text_edit.setMinimumHeight(new_height)
        text_edit.setMaximumHeight(new_height)

    def eventFilter(self, obj, event):
        if event.type() == QEvent.FocusIn:
            self.start_editing()
        elif event.type() == QEvent.FocusOut:
            self.finish_editing()
        return super().eventFilter(obj, event)

    def start_editing(self):
        self.is_editing = True
        self.expand_card(force=True)

    def finish_editing(self):
        self.is_editing = False
        if not self.underMouse():
            self.collapse_card()

    def enterEvent(self, event):
        self.expand_card()
        super().enterEvent(event)

    def leaveEvent(self, event):
        if not self.is_editing:
            self.collapse_card()
        super().leaveEvent(event)

    def expand_card(self, force=False):
        if not self.is_expanded or force:
            self.is_expanded = True
            self.translate.show()

    def collapse_card(self):
        if self.is_expanded and not self.is_editing:
            self.is_expanded = False
            self.translate.hide()

    def to_sentence_card(self):
        self.sentence_card.translate = self.translate.toPlainText()
        return self.sentence_card

    def set_info(self, sentence_card):
        self.sentence_card.sentence.setPlainText(sentence_card.translate)

    def set_info_from_ai(self, info):
        if info['sentence'] == self.sentence_card.sentence:
            self.translate.setPlainText(info['meaning'])
            self.sentence.setStyleSheet("background-color: rgb(17, 45, 78);")
