import os.path
from striprtf.striprtf import rtf_to_text
from PySide6.QtCore import (Qt, QPropertyAnimation, Signal,
                            QEasingCurve, Signal, QEvent, QTimer)
from PySide6.QtGui import QCursor, QTextCursor, QTextCharFormat, QColor
from PySide6.QtWidgets import QWidget, QMenu, QTextEdit, QFileDialog
from ui import Ui_english_edit_widget
import json


def split_text_by_line(text, max_length=6000):
    """
    按换行符分割文本，并确保每段不超过指定长度

    参数:
    text (str): 需要分割的原始文本
    max_length (int): 每段的最大字符数，默认为1500

    返回:
    list: 分割后的文本段落列表
    """
    if not text:
        return []

    paragraphs = []
    current_paragraph = ""

    # 按行分割文本
    lines = text.split('\n')

    for line in lines:
        # 如果添加当前行后会超过最大长度，则将当前段落添加到结果中并开始新段落
        if len(current_paragraph) + len(line) + 1 > max_length:  # +1 是为换行符
            if current_paragraph:  # 避免添加空段落
                paragraphs.append(current_paragraph)
            current_paragraph = line
        else:
            # 否则将当前行添加到当前段落，并添加换行符
            if current_paragraph:
                current_paragraph += '\n' + line
            else:
                current_paragraph = line  # 处理第一个段落

    # 添加最后一个段落
    if current_paragraph:
        paragraphs.append(current_paragraph)

    return paragraphs


class EnglishEditWidgetPage(QWidget, Ui_english_edit_widget):
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
        page_index = 0
        for key, highlight in self.highlight_dict.items():
            highlight_start = highlight.cursor.selectionStart()
            highlight_end = highlight.cursor.selectionEnd()
            highlight_list.append([key, highlight_start, highlight_end])

        return {
            "page_index": page_index,
            "highlight_list": highlight_list,
        }

    def load_project_info(self, item):
        name = item.data(Qt.UserRole)
        path = "./data/" + name + ".json"
        if not os.path.exists(path):
            self.load_rtf_file(path)  #todo:

        with open(path, 'r', encoding='utf-8') as f:
            self.text_data = json.load(f)
        self.english_edit.setPlainText(self.text_data[0])  # todo: data[0]

        path = "./data/" + name + "_highlight.json"
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
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

    def load_rtf_file(self, save_path):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "选择RTF文件", "", "RTF Files (*.rtf);;All Files (*)"
        )
        with open(file_path) as infile:
            content = infile.read()
            text = rtf_to_text(content)

        long_text = text.replace('‘', '\'').replace('’', '\'')
        segments = split_text_by_line(long_text, max_length=6000)
        self.total_pages = len(segments)

        with open(save_path, 'w', encoding='utf-8') as f:
            json.dump(segments, f, ensure_ascii=False, indent=2)

    def prev_page(self):
        if self.current_page > 1:
            self.current_page -= 1
            self.update_display()

    def next_page(self):
        if self.current_page < self.total_pages:
            self.current_page += 1
            self.update_display()

    def update_display(self):
        self.english_edit.setText(self.text_data[self.current_page - 1])
        # self.page_label.setText(f"第 {self.current_page} 页，共 {self.total_pages} 页")
        self.prev_btn.setEnabled(self.current_page > 1)
        self.next_btn.setEnabled(self.current_page < self.total_pages)
        # self.page_input.clear()

