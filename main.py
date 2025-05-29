import sys
import os
from module import Project
from page import (MainWindowPage, LeftBoxPage, NewDialogPage,
                  HomeWindowPage, EnglishEditWidgetPage, ContainerWidgetPage,
                  WordCardPage, ProjectWidgetListPage)
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QAction, QShortcut, QKeySequence
import json
import base64


class LingThread:
    def __init__(self):
        self.setup_ui()
        self.project_list = []
        self.cur_project_item = None
        self.card_dict = {}
        self.save_path = "./data"
        self.cur_word = None
        if os.path.exists(os.path.join(self.save_path, "project_items.json")):
            self.load_project_items()

    def setup_ui(self):
        self.window = MainWindowPage()

        v_layout = QVBoxLayout(self.window.left_hide_box)
        v_layout.setContentsMargins(0, 0, 0, 0)
        left_box = LeftBoxPage()
        v_layout.addWidget(left_box)
        left_box.show_hide_left_box_signal.connect(self.window.show_hide_left_box)

        self.window.create_new_project_signal.connect(self.create_new_project)

        v_layout_2 = QVBoxLayout(self.window.edit_page)
        v_layout_2.setContentsMargins(0, 0, 0, 0)
        home_page = HomeWindowPage(self.window.main_page)
        v_layout_2.addWidget(home_page)

        self.window.show_hide_word_card_signal.connect(home_page.show_hide_word_card)
        self.window.show_hide_sentence_card_signal.connect(home_page.show_hide_sentence_card)
        self.window.show_hide_ai_chat_card_signal.connect(home_page.show_hide_ai_chat_card)

        v_layout_3 = QVBoxLayout(home_page.edit_widget)
        v_layout_3.setContentsMargins(0, 0, 0, 0)
        self.english_edit_page = EnglishEditWidgetPage(home_page.edit_widget)
        v_layout_3.addWidget(self.english_edit_page)

        self.english_edit_page.create_word_card_signal.connect(self.create_word_card)
        self.english_edit_page.corresponding_word_card_show_signal.connect(self.corresponding_word_card_show)
        self.english_edit_page.load_word_card_signal.connect(self.load_word_card)
        v_layout_4 = QVBoxLayout(home_page.word_card_widget)
        v_layout_4.setContentsMargins(0, 0, 0, 0)
        word_card_container_page = ContainerWidgetPage(home_page.word_card_widget)
        v_layout_4.addWidget(word_card_container_page)

        self.word_card_layout = QVBoxLayout()
        word_card_container_page.contents.setLayout(self.word_card_layout)
        self.word_card_layout.setAlignment(Qt.AlignTop)

        v_layout_5 = QVBoxLayout(self.window.project_list_page)
        v_layout_5.setContentsMargins(0, 0, 0, 0)
        self.project_widget_list = ProjectWidgetListPage(self.window.project_list_page)
        v_layout_5.addWidget(self.project_widget_list)
        self.window.stacked_widget.setCurrentIndex(2)
        self.project_widget_list.item_double_clicked_signal.connect(self.open_item_project)

        shortcut = QShortcut(QKeySequence("Ctrl+S"), self.window)
        shortcut.activated.connect(self.save_current_project_info)

    def load_project_items(self):
        with open("./data/project_items.json", 'r') as f:
            json_data = json.load(f)
        for key, value in json_data.items():
            base64_data = value.get("image", "")
            image_data = base64.b64decode(base64_data)

            pixmap = QPixmap()
            pixmap.loadFromData(image_data)

            project = Project(value.get("name"),
                              value.get("author"),
                              value.get("modified_time"),
                              pixmap)
            self.project_widget_list.add_project(project)

    def create_word_card(self, word):
        self.cur_word = word
        card = WordCardPage(self.window, word)
        self.word_card_layout.addWidget(card)
        self.card_dict[word] = card

    def load_word_card(self, word):
        with open("./data/" + "word_cards.json", 'r') as f:
            data = json.load(f)
        info = data[word]
        card = WordCardPage(self.window, word)
        card.set_info(info)
        self.word_card_layout.addWidget(card)
        self.card_dict[word] = card

    def show(self):
        self.window.show()

    def create_new_project(self):
        new_window = NewDialogPage(self.window)
        new_window.create_new_project_signal.connect(self.add_new_project)
        if new_window.exec():
            return

    def add_new_project(self, image_path, name, author, time):
        print(image_path, name, author, time)
        project = Project(name, author, time, image_path)
        self.project_widget_list.add_project(project)

    def corresponding_word_card_show(self, word):
        if self.cur_word is not None:
            self.card_dict[self.cur_word].collapse_card()
        if word in self.card_dict:
            self.card_dict[word].expand_card()
            self.cur_word = word

    def open_item_project(self, item):
        self.cur_project_item = item
        self.window.stacked_widget.setCurrentIndex(1)
        self.english_edit_page.load_project_info(self.cur_project_item)

    def save_current_project_info(self):
        if self.cur_project_item is not None:
            name = self.cur_project_item.data(Qt.UserRole)
            path = os.path.join(self.save_path, name + ".json")
            result = self.english_edit_page.to_dict()
            with open(path, 'w', encoding='utf-8') as f:
                json.dump(result, f, ensure_ascii=False, indent=2)
            word_cards_json = {}
            for word, info in self.card_dict.items():
                word_cards_json[word] = info.to_dict()
            path = os.path.join(self.save_path, "word_cards.json")
            with open(path, 'w', encoding='utf-8') as f:
                json.dump(word_cards_json, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    LT = LingThread()
    LT.show()

    app.exec()
