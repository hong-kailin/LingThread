from ui import Ui_word_card_widget
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QPushButton,
                               QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
from PySide6.QtCore import QEvent, QTimer, Qt, Signal
from database import WordCard
import time


class WordCardWidgetPage(QFrame, Ui_word_card_widget):
    parser_word_signal = Signal(str)

    def __init__(self, parent, word, word_parser_assistant=None):
        super().__init__(parent)
        self.setupUi(self)
        self.word_parser_assistant = word_parser_assistant
        self.parser_word_signal.connect(self.word_parser_assistant.parser_word)
        self.word_parser_assistant.return_result_signal.connect(self.set_info_from_ai)
        self.other_edit.installEventFilter(self)
        self.mean_edit.installEventFilter(self)
        self.pronunciation_edit.installEventFilter(self)
        self.mean_remember_edit.installEventFilter(self)
        self.pronunciation_remember_edit.installEventFilter(self)

        self.other_edit.hide()
        self.mean_edit.hide()
        self.pronunciation_edit.hide()
        self.mean_remember_edit.hide()
        self.pronunciation_remember_edit.hide()
        self.word_card = WordCard(word)
        self.label.setText(self.word_card.word)

        self.is_expanded = False
        self.is_editing = False
        self.timer = QTimer(self)
        self.label.mousePressEvent = self.label_mouse_press_event
        self.label.mouseReleaseEvent = self.label_mouse_release_event
        self.timer.timeout.connect(self.check_long_press)

    def label_mouse_press_event(self, event):
        if event.button() == Qt.LeftButton:
            self.press_time = time.time()
            self.timer.start(100)
        super().mousePressEvent(event)

    def label_mouse_release_event(self, event):
        if event.button() == Qt.LeftButton:
            self.timer.stop()
            if time.time() - self.press_time < 2:
                self.label.setStyleSheet("background-color: lightblue; font-size: 18px;")
        super().mouseReleaseEvent(event)

    def check_long_press(self):
        if time.time() - self.press_time >= 2:
            self.timer.stop()
            self.label.setStyleSheet("background-color: lightgreen; font-size: 18px;")
            self.parser_word_signal.emit(self.word_card.word)

    def mean_height_change(self):
        self.adjust_text_edit_height(self.mean_edit)

    def pronunciation_height_change(self):
        self.adjust_text_edit_height(self.pronunciation_edit)

    def mean_remember_height_change(self):
        self.adjust_text_edit_height(self.mean_remember_edit)

    def pronunciation_remember_height_change(self):
        self.adjust_text_edit_height(self.pronunciation_remember_edit)

    def other_height_change(self):
        self.adjust_text_edit_height(self.other_edit)

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
            self.other_edit.show()
            self.mean_edit.show()
            self.pronunciation_edit.show()
            self.mean_remember_edit.show()
            self.pronunciation_remember_edit.show()
            self.other_height_change()
            self.mean_height_change()
            self.mean_remember_height_change()
            self.pronunciation_height_change()
            self.pronunciation_remember_height_change()

    def collapse_card(self):
        if self.is_expanded and not self.is_editing:
            self.is_expanded = False
            self.other_edit.hide()
            self.mean_edit.hide()
            self.pronunciation_edit.hide()
            self.mean_remember_edit.hide()
            self.pronunciation_remember_edit.hide()

    def to_word_card(self):
        self.word_card.mean = self.mean_edit.toPlainText()
        self.word_card.mean_r = self.mean_remember_edit.toPlainText()
        self.word_card.pron = self.pronunciation_edit.toPlainText()
        self.word_card.pron_r = self.pronunciation_remember_edit.toPlainText()
        self.word_card.other = self.other_edit.toPlainText()
        return self.word_card

    def set_info(self, word_card):
        self.other_edit.setPlainText(word_card.other)
        self.mean_edit.setPlainText(word_card.mean)
        self.pronunciation_edit.setPlainText(word_card.pron)
        self.mean_remember_edit.setPlainText(word_card.mean_r)
        self.pronunciation_remember_edit.setPlainText(word_card.pron_r)

    def set_info_from_ai(self, info):
        self.mean_edit.setPlainText(info['meaning'])
        self.pronunciation_edit.setPlainText(info['phonetic'])
        self.mean_remember_edit.setPlainText(info['mnemonic'])
        self.pronunciation_remember_edit.setPlainText(info['pronunciation_tip'])