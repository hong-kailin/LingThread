import sys
from page import (MainWindowPage, LeftBoxPage, NewDialogPage,
                  HomeWindowPage, EnglishEditWidgetPage)
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindowPage()

    v_layout = QVBoxLayout(window.left_hide_box)
    v_layout.setContentsMargins(0, 0, 0, 0)
    left_box = LeftBoxPage()
    v_layout.addWidget(left_box)
    left_box.close_left_box_signal.connect(window.show_hide_left_box)


    def create_new_english_note():
        new_window = NewDialogPage(window)

        def teeee(a, b, c, d):
            print(a, b, c, d)

        new_window.create_new_project_signal.connect(teeee)
        if new_window.exec():
            print("===")


    window.create_new_english_note_signal.connect(create_new_english_note)

    v_layout_2 = QVBoxLayout(window.main_page)
    v_layout_2.setContentsMargins(0, 0, 0, 0)
    home_page = HomeWindowPage(window.main_page)
    v_layout_2.addWidget(home_page)

    window.show_hide_word_card_signal.connect(home_page.show_hide_word_card)
    window.show_hide_sentence_card_signal.connect(home_page.show_hide_sentence_card)
    window.show_hide_ai_chat_card_signal.connect(home_page.show_hide_ai_chat_card)

    v_layout_3 = QVBoxLayout(home_page.edit_widget)
    v_layout_3.setContentsMargins(0, 0, 0, 0)
    english_edit_page = EnglishEditWidgetPage(home_page.edit_widget)
    v_layout_3.addWidget(english_edit_page)

    window.show()
    app.exec()
