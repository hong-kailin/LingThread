from PySide6.QtWidgets import QWidget, QMenu, QTextEdit
from ui import Ui_container_widget
from .word_card_widget_page import WordCardWidgetPage
from database import WordCardDict


class WordCardContainerPage(QWidget, Ui_container_widget):
    def __init__(self, parent=None, path=None, word_parser_assistant=None):
        super().__init__(parent)
        self.setupUi(self)
        self.word_parser_assistant = word_parser_assistant
        self.path = path
        self.card_widget_dict = {}
        self.all_word_card_dict = WordCardDict(path)
        self.cur_word = None
        self.load_word_card_list()

    def scroll_to_card(self, card):
        if card and card.isVisible():
            card_rect = card.geometry()
            scroll_pos = card_rect.top() - 5
            self.scrollArea.verticalScrollBar().setValue(scroll_pos)

    def load_word_card_list(self):
        for word, word_card in self.all_word_card_dict.dict.items():
            self.load_word_card(word_card)

    def load_word_card(self, word_card):
        self.cur_word = word_card.word
        card = WordCardWidgetPage(self, word_card.word, self.word_parser_assistant)
        card.set_info(word_card)
        insert_position = self.container_layout.count() - 1
        self.container_layout.insertWidget(insert_position, card)
        self.card_widget_dict[word_card.word] = card

    def create_new_word_card(self, word):
        self.cur_word = word
        card = WordCardWidgetPage(self, word, self.word_parser_assistant)
        insert_position = self.container_layout.count() - 1
        self.container_layout.insertWidget(insert_position, card)
        self.card_widget_dict[word] = card

    def corresponding_word_card_show(self, word):
        if self.cur_word is not None:
            self.card_widget_dict[self.cur_word].collapse_card()
        if word in self.card_widget_dict:
            self.card_widget_dict[word].expand_card()
            self.cur_word = word
            self.scroll_to_card(self.card_widget_dict[word])

    def update_and_save_word_card_dict(self):
        for word, widget in self.card_widget_dict.items():
            self.all_word_card_dict.append(widget.to_word_card())
        self.all_word_card_dict.save(self.path)
