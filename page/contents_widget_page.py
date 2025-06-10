import asyncio
from PySide6.QtCore import (Qt, QPropertyAnimation, Signal,
                            QEasingCurve, Signal, QEvent, QTimer)
from PySide6.QtGui import QCursor, QTextCursor, QTextCharFormat, QColor
from PySide6.QtWidgets import QWidget, QMenu, QTextEdit, QFileDialog, QMessageBox
from ui import Ui_contents_widget
from agent import Speaker


class ContentsWidgetPage(QWidget, Ui_contents_widget):
    create_word_card_signal = Signal(str)
    create_sentence_card_signal = Signal(str)
    corresponding_word_card_show_signal = Signal(str)
    load_word_card_signal = Signal(str)
    page_number_update_signal = Signal(int)

    def __init__(self, project, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.project = project
        # ====
        self.is_playing = False
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)
        self.speaker = Speaker(self.loop)
        self.speaker.finished.connect(self.on_speaker_finished)
        # ====
        self.highlight_dict = {}
        self.underline_dict = {}
        self.content.setContextMenuPolicy(Qt.CustomContextMenu)
        self.content.viewport().installEventFilter(self)

        self.highlight_format = QTextCharFormat()
        self.highlight_format.setBackground(QColor(150, 20, 70))
        self.highlight_format.setUnderlineStyle(QTextCharFormat.SingleUnderline)
        self.highlight_format.setUnderlineColor(QColor(255, 179, 0))

        self.sentence_underline_format = QTextCharFormat()
        self.sentence_underline_format.setUnderlineStyle(QTextCharFormat.SingleUnderline)
        self.sentence_underline_format.setUnderlineColor(QColor(80, 179, 0))

        self.current_page = 0
        self.load_content_info(self.project.contents[self.current_page],
                               self.project.highlight_words_per_content[self.current_page])

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
            create_sentence_action = menu.addAction("create sentence card")
            create_sentence_action.triggered.connect(lambda: self.create_sentence_card(cursor))
            read_action = menu.addAction("read this sentence")
            read_action.triggered.connect(lambda: self.read_chosen_content(cursor))
            stop_read_action = menu.addAction("stop to read")
            stop_read_action.triggered.connect(self.stop_speaking)
            menu.exec(self.content.mapToGlobal(pos))

    def read_chosen_content(self, cursor):
        selected_text = cursor.selectedText().strip()
        if not selected_text.strip():
            QMessageBox.warning(self, "警告", "请先选择要朗读的文本")
            return
        self.is_playing = True
        self.speaker.set_text(selected_text)
        self.speaker.start()

    def stop_speaking(self):
        self.is_playing = False
        self.speaker.stop()

    def on_speaker_finished(self):
        self.is_playing = False

    def create_word_card(self, cursor):
        selected_text = cursor.selectedText().strip()
        if not selected_text:
            return
        self.create_word_card_signal.emit(selected_text)
        self.add_highlight(cursor)

    def create_sentence_card(self, cursor):
        selected_text = cursor.selectedText().strip()
        if not selected_text:
            return
        self.create_sentence_card_signal.emit(selected_text)
        self.add_sentence_underline(cursor)

    def add_sentence_underline(self, cursor):
        new_cursor = self.content.textCursor()
        start = cursor.selectionStart()
        end = cursor.selectionEnd()
        new_cursor.setPosition(start)
        new_cursor.setPosition(end, QTextCursor.KeepAnchor)

        extra_selection = QTextEdit.ExtraSelection()
        extra_selection.format = self.sentence_underline_format
        extra_selection.cursor = new_cursor

        self.underline_dict[new_cursor.selectedText().strip()] = extra_selection
        self.content.setExtraSelections(list(self.underline_dict.values()))
        self.project.add_underline_info(self.current_page, new_cursor.selectedText().strip(), start, end)

    def add_highlight(self, cursor):
        new_cursor = self.content.textCursor()
        start = cursor.selectionStart()
        end = cursor.selectionEnd()
        new_cursor.setPosition(start)
        new_cursor.setPosition(end, QTextCursor.KeepAnchor)

        extra_selection = QTextEdit.ExtraSelection()
        extra_selection.format = self.highlight_format
        extra_selection.cursor = new_cursor

        self.highlight_dict[new_cursor.selectedText().strip()] = extra_selection
        self.content.setExtraSelections(list(self.highlight_dict.values()))

        self.project.add_highlight_info(self.current_page, new_cursor.selectedText().strip(), start, end)

    def delete_highlight(self, word):
        if word in self.highlight_dict:
            del self.highlight_dict[word]
            self.content.setExtraSelections(list(self.highlight_dict.values()))

    def eventFilter(self, obj, event):
        if event.type() == QEvent.MouseButtonRelease:
            cursor = self.content.textCursor()
            if cursor.hasSelection():
                selected_text = cursor.selectedText()
                self.corresponding_word_card_show_signal.emit(selected_text)
        return super().eventFilter(obj, event)

    def load_content_info(self, content, highlight_list):
        self.content.setPlainText(content)
        for word, [start, end] in highlight_list.items():
            self.load_word_card_signal.emit(word)
            cursor = self.content.textCursor()

            if 0 <= start <= end <= len(self.content.toPlainText()):
                cursor.setPosition(start)
                cursor.setPosition(end, QTextCursor.KeepAnchor)
                self.add_highlight(cursor)

    def prev_page(self):
        if self.current_page > 0:
            self.current_page -= 1
            self.update_display()

    def next_page(self):
        if self.current_page < self.project.total_pages:
            self.current_page += 1
            self.update_display()

    def update_display(self):
        self.load_content_info(self.project.contents[self.current_page],
                               self.project.highlight_words_per_content[self.current_page])
        self.prev_btn.setEnabled(self.current_page > 0)
        self.next_btn.setEnabled(self.current_page < self.project.total_pages)
        self.page_number_update_signal.emit(self.current_page)
