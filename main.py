import sys
import os
from PySide6.QtWidgets import QApplication, QVBoxLayout
from PySide6.QtGui import QPixmap, QAction, QShortcut, QKeySequence, QIcon
from PySide6.QtCore import QEvent, QSize, Signal, Qt

from page import (MainWindowPage, LeftBoxPage, NewDialogPage, ContentsWidgetPage,
                  ProjectWidgetListPage, MainWidgetPage, WordCardContainerPage,
                  AiChatWidgetPage, SentenceCardContainerPage)
from agent import WordParserAssistant, SentenceTranslateAssistant
from database import Project
import json
import base64


class LingThread:
    def __init__(self):
        self.data_save_path = "./data"
        self.cur_project = None
        self.word_parser_assistant = WordParserAssistant()
        self.sentence_translate_assistant = SentenceTranslateAssistant()
        self.main_window = MainWindowPage()
        self.setup_ui()
        self.load_existent_project_info()

        shortcut = QShortcut(QKeySequence("Ctrl+S"), self.main_window)
        shortcut.activated.connect(self.save_current_project_info)

    def setup_ui(self):
        v_layout = QVBoxLayout(self.main_window.left_hide_box)
        v_layout.setContentsMargins(0, 0, 0, 0)
        left_box = LeftBoxPage()
        v_layout.addWidget(left_box)
        left_box.show_hide_left_box_signal.connect(self.main_window.show_hide_left_box)

        v_layout_2 = QVBoxLayout(self.main_window.project_list_page)
        v_layout_2.setContentsMargins(0, 0, 0, 0)
        self.project_widget_list = ProjectWidgetListPage(self.main_window.project_list_page)
        v_layout_2.addWidget(self.project_widget_list)
        self.main_window.stacked_widget.setCurrentIndex(0)
        self.main_window.create_new_project_signal.connect(self.create_new_project)
        self.project_widget_list.item_double_clicked_signal.connect(self.open_item_project)

        v_layout_3 = QVBoxLayout(self.main_window.contents_page)
        v_layout_3.setContentsMargins(0, 0, 0, 0)
        self.main_widget = MainWidgetPage(self.main_window.contents_page)
        v_layout_3.addWidget(self.main_widget)

        self.main_window.show_hide_word_card_signal.connect(self.main_widget.show_hide_word_card)
        self.main_window.show_hide_sentence_card_signal.connect(self.main_widget.show_hide_sentence_card)
        self.main_window.show_hide_ai_chat_card_signal.connect(self.main_widget.show_hide_ai_chat_card)
        self.main_window.show_project_list_signal.connect(self.show_project_list)
        self.main_window.save_current_project_info_signal.connect(self.save_current_project_info)

        v_layout_4 = QVBoxLayout(self.main_widget.word_card_widget)
        v_layout_4.setContentsMargins(0, 0, 0, 0)
        self.word_card_container_page = WordCardContainerPage(self.main_widget.word_card_widget,
                                                              self.data_save_path,
                                                              self.word_parser_assistant)
        v_layout_4.addWidget(self.word_card_container_page)

        v_layout_5 = QVBoxLayout(self.main_widget.ai_chat_widget)
        v_layout_5.setContentsMargins(0, 0, 0, 0)
        self.ai_chat_widget_page = AiChatWidgetPage(self.main_widget.ai_chat_widget)
        v_layout_5.addWidget(self.ai_chat_widget_page)

        v_layout_6 = QVBoxLayout(self.main_widget.sentence_card_widget)
        v_layout_6.setContentsMargins(0, 0, 0, 0)
        self.sentence_card_container_page = SentenceCardContainerPage(self.main_widget.sentence_card_widget,
                                                                      self.data_save_path,
                                                                      self.sentence_translate_assistant)
        v_layout_6.addWidget(self.sentence_card_container_page)

    def show(self):
        self.main_window.show()

    def create_new_project(self):
        new_window = NewDialogPage(self.main_window)

        def _create_new_project(image_path, name, author, modified_time):
            project = Project(name, author, modified_time, image_path, self.data_save_path)
            self.project_widget_list.add_new_project(project)

        new_window.create_new_project_signal.connect(_create_new_project)
        if new_window.exec():
            return

    def load_existent_project_info(self):
        project_info_json_path = os.path.join(self.data_save_path, "project_info.json")
        if os.path.exists(project_info_json_path):
            with open(project_info_json_path, 'r', encoding='utf-8') as f:
                json_data = json.load(f)
            for key, value in json_data.items():
                base64_data = value.get("image", "")
                image_data = base64.b64decode(base64_data)

                pixmap = QPixmap()
                pixmap.loadFromData(image_data)

                project = Project(value.get("name"),
                                  value.get("author"),
                                  value.get("modified_time"),
                                  pixmap,
                                  self.data_save_path)
                self.project_widget_list.add_existent_project(project)

    def open_item_project(self, item):
        self.cur_project = item.data(Qt.UserRole)
        self.cur_project.load_contents(self.main_window)
        # ==========
        v_layout_3 = QVBoxLayout(self.main_widget.content_widget)
        v_layout_3.setContentsMargins(0, 0, 0, 0)
        self.contents_widget_page = ContentsWidgetPage(self.cur_project, self.main_widget.content_widget)
        v_layout_3.addWidget(self.contents_widget_page)
        self.word_card_container_page.delete_word_card_signal.connect(self.contents_widget_page.delete_highlight)
        self.sentence_card_container_page.delete_sentence_card_signal.connect(self.contents_widget_page.delete_underline)
        self.contents_widget_page.create_word_card_signal.connect(self.word_card_container_page.create_new_word_card)
        self.contents_widget_page.create_sentence_card_signal.connect(self.sentence_card_container_page.create_new_sentence_card)
        self.contents_widget_page.corresponding_word_card_show_signal.connect(
            self.word_card_container_page.corresponding_word_card_show)
        self.contents_widget_page.page_number_update_signal.connect(self.main_window.page_number_update)
        self.main_window.stacked_widget.setCurrentIndex(1)

    def save_current_project_info(self):
        if self.cur_project is not None:
            self.cur_project.save_highlight_info()
            self.cur_project.save_underline_info()
        self.word_card_container_page.update_and_save_word_card_dict()
        self.sentence_card_container_page.update_and_save_sentence_card_dict()

    def show_project_list(self):
        self.main_window.stacked_widget.setCurrentIndex(2)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    LT = LingThread()
    LT.show()
    app.exec()
