import sys
import json
import os
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *


class VocabularyCard(QFrame):
    def __init__(self, parent=None, word="", definition="", example=""):
        super().__init__(parent)
        self.parent = parent
        self.word = word
        self.is_expanded = False
        self.is_editing = False
        self.highlight = None

        # 卡片样式设置
        self.setFrameShape(QFrame.StyledPanel)
        self.setLineWidth(1)
        self.setMinimumWidth(180)
        self.setMaximumWidth(280)
        self.setStyleSheet("""
            QFrame {
                background: #f8f9fa;
                border-radius: 5px;
                margin: 5px;
                border: 1px solid #dee2e6;
            }
            QLabel#title {
                font-weight: 500;
                color: #2c3e50;
                padding: 8px 10px;
                font-size: 13px;
                border-bottom: 1px solid #dee2e6;
                qproperty-alignment: AlignCenter;
            }
            QLabel#subtitle {
                font-weight: 500;
                color: #2c3e50;
                padding: 4px 8px;
                font-size: 12px;
                background: #e9ecef;
            }
            QTextEdit {
                border: none;
                padding: 8px;
                font-size: 13px;
                background: white;
                border-bottom: 1px solid #dee2e6;
            }
        """)

        # 主布局
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        # 标题栏
        self.title = QLabel(word)
        self.title.setObjectName("title")
        self.title.setWordWrap(True)
        self.title.setMinimumHeight(36)
        self.title.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        layout.addWidget(self.title)

        # 内容区域
        self.content = QWidget()
        content_layout = QVBoxLayout()
        content_layout.setContentsMargins(0, 0, 0, 0)

        # 解释部分
        self.definition_label = QLabel("解释:")
        self.definition_label.setObjectName("subtitle")
        self.definition_edit = QTextEdit()
        self.definition_edit.setPlaceholderText("输入单词解释...")
        self.definition_edit.setMaximumHeight(80)
        self.definition_edit.installEventFilter(self)
        self.definition_edit.setText(definition)

        # 例句部分
        self.example_label = QLabel("例句:")
        self.example_label.setObjectName("subtitle")
        self.example_edit = QTextEdit()
        self.example_edit.setPlaceholderText("输入例句...")
        self.example_edit.setMaximumHeight(80)
        self.example_edit.installEventFilter(self)
        self.example_edit.setText(example)

        content_layout.addWidget(self.definition_label)
        content_layout.addWidget(self.definition_edit)
        content_layout.addWidget(self.example_label)
        content_layout.addWidget(self.example_edit)

        self.content.setLayout(content_layout)
        self.content.hide()

        layout.addWidget(self.content)
        self.setLayout(layout)

        # 右键菜单
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.show_context_menu)

        # 初始为折叠状态
        self.collapse_card()

    def eventFilter(self, obj, event):
        if obj in [self.definition_edit, self.example_edit]:
            if event.type() == QEvent.FocusIn:
                self.start_editing()
            elif event.type() == QEvent.FocusOut:
                self.finish_editing()
        return super().eventFilter(obj, event)

    def show_context_menu(self, pos):
        menu = QMenu(self)
        delete_action = menu.addAction("删除卡片")
        delete_action.triggered.connect(self.delete_card)
        menu.exec(self.mapToGlobal(pos))

    def delete_card(self):
        self.parent.remove_card(self)

    def start_editing(self):
        self.is_editing = True
        self.expand_card(force=True)

    def finish_editing(self):
        self.is_editing = False
        if not self.underMouse():
            self.collapse_card()

    def enterEvent(self, event):
        self.expand_card()
        super().enterEvent(event)

    def leaveEvent(self, event):
        if not self.is_editing:
            self.collapse_card()
        super().leaveEvent(event)

    def expand_card(self, force=False):
        if not self.is_expanded or force:
            self.is_expanded = True
            self.content.show()
            self.setFixedHeight(260)
            # 调用父窗口的方法滚动到该卡片
            # if self.parent:
            #     self.parent.scroll_to_card(self)

    def collapse_card(self):
        if self.is_expanded and not self.is_editing:
            self.is_expanded = False
            self.content.hide()
            self.setFixedHeight(50)

    def to_dict(self):
        """将卡片数据转换为字典，用于保存"""
        return {
            "word": self.word,
            "definition": self.definition_edit.toPlainText(),
            "example": self.example_edit.toPlainText(),
            "highlight_start": self.highlight.cursor.selectionStart() if self.highlight else 0,
            "highlight_end": self.highlight.cursor.selectionEnd() if self.highlight else 0
        }


class MainWindow(QMainWindow):
    DATA_FILE = os.path.join(os.path.expanduser("~"), ".vocabulary_card_data.json")

    def __init__(self):
        super().__init__()
        self.cards = []
        self.highlights = []
        self.init_ui()
        self.load_data()  # 加载保存的数据

    def init_ui(self):
        self.setWindowTitle("智能单词卡片")
        self.setGeometry(100, 100, 1000, 600)

        # 主布局
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QHBoxLayout()
        main_widget.setLayout(layout)

        # 左侧文本区域
        self.text_edit = QTextEdit()
        self.text_edit.setStyleSheet("""
            QTextEdit {
                font-size: 14px;
                padding: 12px;
                selection-background-color: #b3d9ff;
            }
        """)
        layout.addWidget(self.text_edit, 3)

        # 右侧卡片区域（带滚动条）
        self.card_scroll = QScrollArea()
        self.card_scroll.setWidgetResizable(True)
        self.card_widget = QWidget()
        self.card_layout = QVBoxLayout()
        self.card_layout.setAlignment(Qt.AlignTop)
        self.card_layout.setContentsMargins(5, 5, 5, 5)
        self.card_layout.setSpacing(5)
        self.card_widget.setLayout(self.card_layout)
        self.card_scroll.setWidget(self.card_widget)
        layout.addWidget(self.card_scroll, 1)

        # 文本编辑器的右键菜单
        self.text_edit.setContextMenuPolicy(Qt.CustomContextMenu)
        self.text_edit.customContextMenuRequested.connect(self.show_text_menu)

        # 安装事件过滤器
        self.text_edit.viewport().installEventFilter(self)

    def eventFilter(self, obj, event):
        if obj == self.text_edit.viewport() and event.type() == QEvent.MouseMove:
            pos = event.pos()
            cursor = self.text_edit.cursorForPosition(pos)
            current_card = None

            # 检查当前鼠标位置是否在某个高亮单词上
            for card in self.cards:
                if card.highlight:
                    highlight = card.highlight.cursor
                    if highlight.selectionStart() <= cursor.position() <= highlight.selectionEnd():
                        # 如果找到匹配的卡片，展开它并标记为当前卡片
                        card.expand_card()
                        current_card = card
                    elif not card.underMouse() and not card.is_editing:
                        # 其他卡片折叠
                        card.collapse_card()

            # 如果找到了当前卡片，滚动到该卡片
            if current_card:
                self.scroll_to_card(current_card)

        return super().eventFilter(obj, event)

    def show_text_menu(self, pos):
        cursor = self.text_edit.textCursor()
        if cursor.hasSelection():
            menu = QMenu(self)
            create_action = menu.addAction("创建卡片")
            create_action.triggered.connect(lambda: self.create_card(cursor))
            menu.exec(self.text_edit.mapToGlobal(pos))

    def create_card(self, cursor):
        selected_text = cursor.selectedText().strip()
        if not selected_text:
            return

        # 检查是否已存在相同单词的卡片
        for card in self.cards:
            if card.word == selected_text:
                card.expand_card(force=True)
                return

        # 创建新卡片
        elided_word = self.elide_text(selected_text, max_length=25)
        card = VocabularyCard(self, elided_word)
        card.word = selected_text  # 保存完整单词

        # 将新卡片添加到布局
        self.card_layout.addWidget(card)
        self.cards.append(card)

        # 添加高亮
        highlight = self.add_highlight(cursor)
        card.highlight = highlight

    def elide_text(self, text, max_length=25):
        """处理超长文本，添加省略号"""
        if len(text) > max_length:
            return text[:max_length - 3] + "..."
        return text

    def add_highlight(self, cursor):
        new_cursor = self.text_edit.textCursor()
        new_cursor.setPosition(cursor.selectionStart())
        new_cursor.setPosition(cursor.selectionEnd(), QTextCursor.KeepAnchor)

        format = QTextCharFormat()
        format.setBackground(QColor(255, 245, 157))
        format.setUnderlineStyle(QTextCharFormat.SingleUnderline)
        format.setUnderlineColor(QColor(255, 179, 0))

        extra_selection = QTextEdit.ExtraSelection()
        extra_selection.format = format
        extra_selection.cursor = new_cursor

        self.highlights.append(extra_selection)
        self.text_edit.setExtraSelections(self.highlights)
        return extra_selection

    def remove_card(self, card):
        # 移除高亮
        if card.highlight in self.highlights:
            self.highlights.remove(card.highlight)
            self.text_edit.setExtraSelections(self.highlights)

        # 移除卡片
        if card in self.cards:
            self.cards.remove(card)
            card.deleteLater()

    def scroll_to_card(self, card):
        """滚动到指定卡片，使其显示在滚动区域的顶部"""
        if card and card.isVisible():
            # 获取卡片在布局中的位置
            card_rect = card.geometry()
            # 计算需要滚动的距离
            scroll_pos = card_rect.top() - 5  # 减去一些边距

            # 设置滚动条位置
            self.card_scroll.verticalScrollBar().setValue(scroll_pos)

    def closeEvent(self, event):
        """窗口关闭时保存数据"""
        self.save_data()
        event.accept()

    def save_data(self):
        """保存数据到文件"""
        data = {
            "text_content": self.text_edit.toPlainText(),
            "cards": [card.to_dict() for card in self.cards]
        }

        try:
            with open(self.DATA_FILE, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"保存数据失败: {e}")

    def load_data(self):
        """从文件加载数据"""
        if not os.path.exists(self.DATA_FILE):
            return

        try:
            with open(self.DATA_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)

            # 恢复文本内容
            self.text_edit.setPlainText(data.get("text_content", ""))

            # 恢复卡片
            for card_data in data.get("cards", []):
                word = card_data["word"]
                definition = card_data["definition"]
                example = card_data["example"]

                # 创建卡片
                elided_word = self.elide_text(word, max_length=25)
                card = VocabularyCard(self, elided_word, definition, example)
                card.word = word

                # 将卡片添加到布局
                self.card_layout.addWidget(card)
                self.cards.append(card)

                # 恢复高亮
                cursor = self.text_edit.textCursor()
                start = card_data["highlight_start"]
                end = card_data["highlight_end"]

                # 确保位置有效
                if 0 <= start <= end <= len(self.text_edit.toPlainText()):
                    cursor.setPosition(start)
                    cursor.setPosition(end, QTextCursor.KeepAnchor)
                    highlight = self.add_highlight(cursor)
                    card.highlight = highlight

        except Exception as e:
            print(f"加载数据失败: {e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # 设置默认字体（可选）
    font = QFont()
    font.setFamily("Microsoft YaHei")
    font.setPointSize(10)
    app.setFont(font)

    window = MainWindow()
    window.show()
    sys.exit(app.exec())