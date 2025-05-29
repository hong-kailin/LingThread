from ui import Ui_word_card
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QPushButton,
                               QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
from PySide6.QtCore import QEvent


class WordCardPage(QFrame, Ui_word_card):
    def __init__(self, parent, word):
        super().__init__(parent)
        self.setupUi(self)

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
        self.word = word
        self.label.setText(self.word)

        self.is_expanded = False
        self.is_editing = False

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

    def collapse_card(self):
        if self.is_expanded and not self.is_editing:
            self.is_expanded = False
            self.other_edit.hide()
            self.mean_edit.hide()
            self.pronunciation_edit.hide()
            self.mean_remember_edit.hide()
            self.pronunciation_remember_edit.hide()

    def to_dict(self):
        return {
            "word": self.word,
            "mean": self.mean_edit.toPlainText(),
            "mean_remember": self.mean_remember_edit.toPlainText(),
            "pronunciation": self.pronunciation_edit.toPlainText(),
            "pronunciation_remember": self.pronunciation_remember_edit.toPlainText(),
            "other": self.other_edit.toPlainText()
        }

    def set_info(self, info):
        self.other_edit.setPlainText(info.get("other", ""))
        self.mean_edit.setPlainText(info.get("mean", ""))
        self.pronunciation_edit.setPlainText(info.get("pronunciation", ""))
        self.mean_remember_edit.setPlainText(info.get("mean_remember", ""))
        self.pronunciation_remember_edit.setPlainText(info.get("pronunciation_remember", ""))
