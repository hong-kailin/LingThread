from PySide6.QtCore import Qt, QPropertyAnimation, Signal, QEasingCurve
from PySide6.QtWidgets import QWidget
from ui import Ui_home_widget


class HomeWindowPage(QWidget, Ui_home_widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ai_chat_widget.setGeometry(self.ai_chat_widget.x(), self.ai_chat_widget.y(), 0,
                                        self.ai_chat_widget.sizeHint().height())
        self.word_card_widget.setGeometry(self.word_card_widget.x(), self.word_card_widget.y(), 0,
                                        self.word_card_widget.sizeHint().height())
        self.sentence_card_widget.setGeometry(self.sentence_card_widget.x(), self.sentence_card_widget.y(), 0,
                                          self.sentence_card_widget.sizeHint().height())
        self.time_amimation = 500

    def show_hide_card(self, widget):
        self.animation = QPropertyAnimation(widget, b"width")
        self.animation.setDuration(self.time_amimation)
        if widget.width() == 0:
            self.animation.setStartValue(0)
            self.animation.setEndValue(240)
        else:
            self.animation.setStartValue(240)
            self.animation.setEndValue(0)
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()

    def show_hide_word_card(self):
        self.show_hide_card(self.word_card_widget)

    def show_hide_sentence_card(self):
        self.show_hide_card(self.sentence_card_widget)

    def show_hide_ai_chat_card(self):
        self.show_hide_card(self.ai_chat_widget)
