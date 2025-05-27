import sys
from page import (MainWindowPage, LeftBoxPage, NewDialogPage,
                  HomeWindowPage, EnglishEditWidgetPage, ContainerWidgetPage,
                  WordCardPage, ProjectWidgetListPage)
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout
from PySide6.QtCore import Qt


class LingThread:
    def __init__(self):
        self.card_dict = {}
        self.window = MainWindowPage()

        v_layout = QVBoxLayout(self.window.left_hide_box)
        v_layout.setContentsMargins(0, 0, 0, 0)
        left_box = LeftBoxPage()
        v_layout.addWidget(left_box)
        left_box.show_hide_left_box_signal.connect(self.window.show_hide_left_box)

        self.window.create_new_english_note_signal.connect(self.create_new_english_note)

        v_layout_2 = QVBoxLayout(self.window.edit_page)
        v_layout_2.setContentsMargins(0, 0, 0, 0)
        home_page = HomeWindowPage(self.window.main_page)
        v_layout_2.addWidget(home_page)

        self.window.show_hide_word_card_signal.connect(home_page.show_hide_word_card)
        self.window.show_hide_sentence_card_signal.connect(home_page.show_hide_sentence_card)
        self.window.show_hide_ai_chat_card_signal.connect(home_page.show_hide_ai_chat_card)

        v_layout_3 = QVBoxLayout(home_page.edit_widget)
        v_layout_3.setContentsMargins(0, 0, 0, 0)
        english_edit_page = EnglishEditWidgetPage(home_page.edit_widget)
        v_layout_3.addWidget(english_edit_page)

        english_edit_page.create_word_card_signal.connect(self.create_word_card)
        english_edit_page.corresponding_word_card_show_signal.connect(self.corresponding_word_card_show)

        v_layout_4 = QVBoxLayout(home_page.word_card_widget)
        v_layout_4.setContentsMargins(0, 0, 0, 0)
        word_card_container_page = ContainerWidgetPage(home_page.word_card_widget)
        v_layout_4.addWidget(word_card_container_page)

        self.word_card_layout = QVBoxLayout()
        word_card_container_page.contents.setLayout(self.word_card_layout)
        self.word_card_layout.setAlignment(Qt.AlignTop)

        v_layout_5 = QVBoxLayout(self.window.project_list_page)
        v_layout_5.setContentsMargins(0, 0, 0, 0)
        self.project_widget_list = ProjectWidgetListPage(self.window.main_page)
        v_layout_5.addWidget(self.project_widget_list)
        self.window.stacked_widget.setCurrentIndex(2)

    def create_word_card(self, word):
        card = WordCardPage(self.window, word)
        self.word_card_layout.addWidget(card)
        self.card_dict[word] = card

    def show(self):
        self.window.show()

    def create_new_english_note(self):
        new_window = NewDialogPage(self.window)

        def teeee(a, b, c, d):
            print(a, b, c, d)

        new_window.create_new_project_signal.connect(teeee)
        if new_window.exec():
            print("===")

    def corresponding_word_card_show(self, word):
        if word in self.card_dict:
            self.card_dict[word].expand_card()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    LT = LingThread()
    LT.show()

    app.exec()
