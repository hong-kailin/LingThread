from PySide6.QtCore import QObject, QPropertyAnimation, Property, QEasingCurve
from PySide6.QtWidgets import QWidget
from ui import Ui_main_widget


class MainWidgetPage(QWidget, Ui_main_widget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.ai_chat_widget.hide()
        self.word_card_widget.hide()
        self.sentence_card_widget.hide()

        self.widgets = [self.ai_chat_widget, self.word_card_widget, self.sentence_card_widget]

    def show_hide_card(self, widget_index):
        sizes = self.splitter.sizes()
        if self.widgets[widget_index].isVisible():
            self.widgets[widget_index].hide()
            hided_width = sizes[widget_index]
            sizes[0] += hided_width
            sizes[widget_index+1] = 0
        else:
            self.widgets[widget_index].show()
            sizes[0] -= 200
            sizes[widget_index+1] = 200
        self.splitter.setSizes(sizes)

    def show_hide_word_card(self):
        self.show_hide_card(1)

    def show_hide_sentence_card(self):
        self.show_hide_card(2)

    def show_hide_ai_chat_card(self):
        self.show_hide_card(0)
