from PySide6.QtWidgets import QWidget, QMenu, QTextEdit
from ui import Ui_container_widget
from .sentence_card_widget_page import SentenceCardWidgetPage
from database import SentenceCard, SentenceCardDict
from PySide6.QtCore import QEvent, QTimer, Qt, Signal


class SentenceCardContainerPage(QWidget, Ui_container_widget):
    delete_sentence_card_signal = Signal(str)

    def __init__(self, parent=None, path=None, sentence_parser_assistant=None):
        super().__init__(parent)
        self.setupUi(self)
        self.sentence_parser_assistant = sentence_parser_assistant
        self.path = path
        self.card_widget_dict = {}
        self.all_sentence_card_dict = SentenceCardDict(path)
        self.cur_sentence = None
        self.load_sentence_card_list()

    def scroll_to_card(self, card):
        if card and card.isVisible():
            card_rect = card.geometry()
            scroll_pos = card_rect.top() - 5
            self.scrollArea.verticalScrollBar().setValue(scroll_pos)

    def load_sentence_card_list(self):
        for sentence, sentence_card in self.all_sentence_card_dict.dict.items():
            self.load_sentence_card(sentence_card)

    def load_sentence_card(self, sentence_card):
        self.cur_sentence = sentence_card.sentence
        card = SentenceCardWidgetPage(self, sentence_card.sentence, self.sentence_parser_assistant)
        card.set_info(sentence_card)
        insert_position = self.container_layout.count() - 1
        self.container_layout.insertWidget(insert_position, card)
        self.card_widget_dict[sentence_card.sentence] = card

    def delete_sentence_card(self, sentence):
        self.card_widget_dict[sentence].deleteLater()
        del self.card_widget_dict[sentence]
        self.all_sentence_card_dict.delete(sentence)
        self.delete_sentence_card_signal.emit(sentence)

    def create_new_sentence_card(self, sentence):
        self.cur_sentence = sentence
        card = SentenceCardWidgetPage(self, sentence, self.sentence_parser_assistant)
        insert_position = self.container_layout.count() - 1
        self.container_layout.insertWidget(insert_position, card)
        self.card_widget_dict[sentence] = card

    def corresponding_word_card_show(self, word):
        if self.cur_sentence is not None and self.cur_sentence in self.card_widget_dict:
            self.card_widget_dict[self.cur_sentence].collapse_card()
        if word in self.card_widget_dict:
            self.card_widget_dict[word].expand_card()
            self.cur_sentence = word
            self.scroll_to_card(self.card_widget_dict[word])

    def update_and_save_sentence_card_dict(self):
        for word, widget in self.card_widget_dict.items():
            self.all_sentence_card_dict.append(widget.to_sentence_card())
        self.all_sentence_card_dict.save(self.path)
