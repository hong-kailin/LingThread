import os.path

from PySide6.QtCore import (Qt, QPropertyAnimation, Signal,
                            QEasingCurve, Signal, QEvent, QTimer)
from PySide6.QtGui import QCursor, QTextCursor, QTextCharFormat, QColor
from PySide6.QtWidgets import QWidget, QMenu, QTextEdit, QFileDialog
from ui import Ui_contents_widget
import json


class ContentsWidgetPage(QWidget, Ui_contents_widget):
    create_word_card_signal = Signal(str)
    corresponding_word_card_show_signal = Signal(str)
    load_word_card_signal = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.current_page = 1
        self.total_pages = 0
        self.text_data = []
        self.highlight_dict = {}
        self.content.setContextMenuPolicy(Qt.CustomContextMenu)
        self.content.viewport().installEventFilter(self)

        self.highlight_format = QTextCharFormat()
        self.highlight_format.setBackground(QColor(255, 245, 157))
        self.highlight_format.setUnderlineStyle(QTextCharFormat.SingleUnderline)
        self.highlight_format.setUnderlineColor(QColor(255, 179, 0))

    def show_text_menu(self, pos):
        cursor = self.content.textCursor()
        if cursor.hasSelection():
            menu = QMenu(self)
            menu.setStyleSheet("""
                QMenu::item {
                    color: black;
                    padding: 6px 24px;
                    background-color: transparent;
                }

                QMenu::item:selected {
                    background-color: #e0e7ff;
                }

                QMenu::separator {
                    height: 1px;
                    background: #eee;
                    margin: 4px 8px;
                }
            """)
            create_action = menu.addAction("create word card")
            create_action.triggered.connect(lambda: self.create_word_card(cursor))
            menu.exec(self.content.mapToGlobal(pos))

    def create_word_card(self, cursor):
        selected_text = cursor.selectedText().strip()
        if not selected_text:
            return
        self.create_word_card_signal.emit(selected_text)
        self.add_highlight(cursor)

    def add_highlight(self, cursor):
        new_cursor = self.content.textCursor()
        new_cursor.setPosition(cursor.selectionStart())
        new_cursor.setPosition(cursor.selectionEnd(), QTextCursor.KeepAnchor)

        extra_selection = QTextEdit.ExtraSelection()
        extra_selection.format = self.highlight_format
        extra_selection.cursor = new_cursor

        self.highlight_dict[new_cursor.selectedText().strip()] = extra_selection
        self.content.setExtraSelections(list(self.highlight_dict.values()))

    def eventFilter(self, obj, event):
        if event.type() == QEvent.MouseButtonRelease:
            cursor = self.content.textCursor()
            if cursor.hasSelection():
                selected_text = cursor.selectedText()
                self.corresponding_word_card_show_signal.emit(selected_text)
        return super().eventFilter(obj, event)

    def save_cur_page_data(self):
        highlight_list = []
        page_index = 0
        for key, highlight in self.highlight_dict.items():
            highlight_start = highlight.cursor.selectionStart()
            highlight_end = highlight.cursor.selectionEnd()
            highlight_list.append([key, highlight_start, highlight_end])

        return {
            "page_index": page_index,
            "highlight_list": highlight_list,
        }

    def load_content_info(self, content, highlight_list):
        self.content.setPlainText(content)
        for highlight in highlight_list:
            word = highlight[0]
            self.load_word_card_signal.emit(word)
            cursor = self.content.textCursor()
            start = highlight[1]
            end = highlight[2]

            if 0 <= start <= end <= len(self.content.toPlainText()):
                cursor.setPosition(start)
                cursor.setPosition(end, QTextCursor.KeepAnchor)
                self.add_highlight(cursor)

    def prev_page(self):
        if self.current_page > 1:
            self.current_page -= 1
            self.update_display()

    def next_page(self):
        if self.current_page < self.total_pages:
            self.current_page += 1
            self.update_display()

    def update_display(self):
        self.content.setText(self.text_data[self.current_page - 1])
        # self.page_label.setText(f"第 {self.current_page} 页，共 {self.total_pages} 页")
        self.prev_btn.setEnabled(self.current_page > 1)
        self.next_btn.setEnabled(self.current_page < self.total_pages)
        # self.page_input.clear()
