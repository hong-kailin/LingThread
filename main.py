import sys
from page import (MainWindowPage, LeftBoxPage, NewDialogPage,
                  HomeWindowPage, EnglishEditWidgetPage, ContainerWidgetPage,
                  WordCardPage)
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout


class LingThread:
    def __init__(self):
        self.window = MainWindowPage()

        v_layout = QVBoxLayout(self.window.left_hide_box)
        v_layout.setContentsMargins(0, 0, 0, 0)
        left_box = LeftBoxPage()
        v_layout.addWidget(left_box)
        left_box.close_left_box_signal.connect(self.window.show_hide_left_box)

        self.window.create_new_english_note_signal.connect(self.create_new_english_note)

        v_layout_2 = QVBoxLayout(self.window.main_page)
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

        v_layout_4 = QVBoxLayout(home_page.word_card_widget)
        v_layout_4.setContentsMargins(0, 0, 0, 0)
        container_page = ContainerWidgetPage(home_page.word_card_widget)
        v_layout_4.addWidget(container_page)

    def create_word_card(self, word):
        print("===", word)

    def show(self):
        self.window.show()

    def create_new_english_note(self):
        new_window = NewDialogPage(self.window)

        def teeee(a, b, c, d):
            print(a, b, c, d)

        new_window.create_new_project_signal.connect(teeee)
        if new_window.exec():
            print("===")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # LT = LingThread()
    # LT.show()
    card = WordCardPage()
    card.show()
    app.exec()
