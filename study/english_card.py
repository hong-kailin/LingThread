import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class VocabularyCard(QFrame):
    def __init__(self, parent=None, word=""):
        super().__init__(parent)
        self.parent = parent
        self.word = word
        self.is_expanded = False
        self.is_editing = False
        self.highlight = None

        # 卡片样式设置
        self.setFrameShape(QFrame.StyledPanel)
        self.setLineWidth(1)
        self.setMinimumWidth(180)  # 保证足够显示空间
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
            QTextEdit {
                border: none;
                padding: 8px;
                font-size: 13px;
                background: white;
            }
        """)

        # 主布局
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        # 标题栏（优化显示）
        self.title = QLabel(word)
        self.title.setObjectName("title")
        self.title.setWordWrap(True)  # 允许自动换行
        self.title.setMinimumHeight(36)  # 保证两行文字高度
        self.title.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        layout.addWidget(self.title)

        # 内容区域
        self.content = QWidget()
        content_layout = QVBoxLayout()
        content_layout.setContentsMargins(0, 0, 0, 0)
        self.text_edit = QTextEdit()
        self.text_edit.setPlaceholderText("输入解释或例句...")
        self.text_edit.setMaximumHeight(120)

        # 焦点事件处理
        self.text_edit.installEventFilter(self)

        content_layout.addWidget(self.text_edit)
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
        if obj == self.text_edit:
            if event.type() == QEvent.FocusIn:
                self.start_editing()
            elif event.type() == QEvent.FocusOut:
                self.finish_editing()
        return super().eventFilter(obj, event)

    def show_context_menu(self, pos):
        menu = QMenu(self)
        delete_action = menu.addAction("删除卡片")
        delete_action.triggered.connect(self.delete_card)
        menu.exec_(self.mapToGlobal(pos))

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
            self.setFixedHeight(200)  # 展开高度

    def collapse_card(self):
        if self.is_expanded and not self.is_editing:
            self.is_expanded = False
            self.content.hide()
            self.setFixedHeight(50)  # 折叠高度（保证显示两行文字）


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.cards = []
        self.highlights = []
        self.init_ui()

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
        self.text_edit.setPlainText("在此输入或粘贴您的文本内容...")
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
            for card in self.cards:
                if not card.is_editing:
                    highlight = card.highlight.cursor
                    if highlight.selectionStart() <= cursor.position() <= highlight.selectionEnd():
                        card.expand_card()
                    elif not card.underMouse():
                        card.collapse_card()
        return super().eventFilter(obj, event)

    def show_text_menu(self, pos):
        cursor = self.text_edit.textCursor()
        if cursor.hasSelection():
            menu = QMenu(self)
            create_action = menu.addAction("创建卡片")
            create_action.triggered.connect(lambda: self.create_card(cursor))
            menu.exec_(self.text_edit.mapToGlobal(pos))

    def create_card(self, cursor):
        selected_text = cursor.selectedText().strip()
        if not selected_text:
            return

        # 检查是否已存在相同单词的卡片
        for card in self.cards:
            if card.word == selected_text:
                card.expand_card(force=True)
                return

        # 创建新卡片（自动处理长单词）
        elided_word = self.elide_text(selected_text, max_length=25)
        card = VocabularyCard(self, elided_word)
        card.word = selected_text  # 保存完整单词

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
        format.setBackground(QColor(255, 245, 157))  # 浅黄色高亮
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


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # 设置默认字体（可选）
    font = QFont()
    font.setFamily("Microsoft YaHei")
    font.setPointSize(10)
    app.setFont(font)

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())