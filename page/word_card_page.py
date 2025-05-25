from ui import Ui_word_card
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QPushButton,
                               QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)


class WordCardPage(QFrame, Ui_word_card):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

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

        text_edit.setFixedHeight(new_height)
