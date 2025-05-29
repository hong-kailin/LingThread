import os.path

from PySide6.QtCore import (Qt, QPropertyAnimation, Signal,
                            QEasingCurve, Signal, QEvent, QTimer)
from PySide6.QtGui import QCursor, QTextCursor, QTextCharFormat, QColor
from PySide6.QtWidgets import QWidget, QMenu, QTextEdit
from ui import Ui_english_edit_widget
import json


class EnglishEditWidgetPage(QWidget, Ui_english_edit_widget):
    create_word_card_signal = Signal(str)
    corresponding_word_card_show_signal = Signal(str)
    load_word_card_signal = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.highlight_dict = {}
        self.english_edit.setContextMenuPolicy(Qt.CustomContextMenu)
        self.english_edit.viewport().installEventFilter(self)

        self.highlight_format = QTextCharFormat()
        self.highlight_format.setBackground(QColor(255, 245, 157))
        self.highlight_format.setUnderlineStyle(QTextCharFormat.SingleUnderline)
        self.highlight_format.setUnderlineColor(QColor(255, 179, 0))

    def show_text_menu(self, pos):
        cursor = self.english_edit.textCursor()
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
            create_action = menu.addAction("create card")
            create_action.triggered.connect(lambda: self.create_card(cursor))
            menu.exec(self.english_edit.mapToGlobal(pos))

    def create_card(self, cursor):
        selected_text = cursor.selectedText().strip()
        print(selected_text)
        if not selected_text:
            return
        # create card
        self.create_word_card_signal.emit(selected_text)
        # ====
        highlight = self.add_highlight(cursor)

    def add_highlight(self, cursor):
        new_cursor = self.english_edit.textCursor()
        new_cursor.setPosition(cursor.selectionStart())
        new_cursor.setPosition(cursor.selectionEnd(), QTextCursor.KeepAnchor)

        extra_selection = QTextEdit.ExtraSelection()
        extra_selection.format = self.highlight_format
        extra_selection.cursor = new_cursor

        self.highlight_dict[new_cursor.selectedText().strip()] = extra_selection
        self.english_edit.setExtraSelections(list(self.highlight_dict.values()))
        return extra_selection

    def eventFilter(self, obj, event):
        if event.type() == QEvent.MouseButtonRelease:
            cursor = self.english_edit.textCursor()
            if cursor.hasSelection():
                selected_text = cursor.selectedText()
                self.corresponding_word_card_show_signal.emit(selected_text)
        return super().eventFilter(obj, event)

    def to_dict(self):
        highlight_list = []
        content = self.english_edit.toPlainText()
        for key, highlight in self.highlight_dict.items():
            highlight_start = highlight.cursor.selectionStart()
            highlight_end = highlight.cursor.selectionEnd()
            highlight_list.append([key, highlight_start, highlight_end])

        return {
            "content": content,
            "highlight_list": highlight_list,
        }

    def load_project_info(self, item):
        name = item.data(Qt.UserRole)
        path = "./data/" + name + ".json"
        if os.path.exists(path):
            with open(path, 'r') as f:
                data = json.load(f)

            self.english_edit.setPlainText(data.get("content", ""))

            for highlight in data.get("highlight_list", []):
                word = highlight[0]
                self.load_word_card_signal.emit(word)
                cursor = self.english_edit.textCursor()
                start = highlight[1]
                end = highlight[2]

                if 0 <= start <= end <= len(self.english_edit.toPlainText()):
                    cursor.setPosition(start)
                    cursor.setPosition(end, QTextCursor.KeepAnchor)
                    highlight = self.add_highlight(cursor)
