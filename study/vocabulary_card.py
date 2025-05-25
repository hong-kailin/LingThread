import sys
from PySide6.QtWidgets import (QApplication, QWidget, QLabel, QTextEdit,
                               QVBoxLayout, QSizePolicy)
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QFont, QFontMetrics


class VocabularyCard(QWidget):
    def __init__(self, word="Hello", parent=None):
        super().__init__(parent)
        self.initUI(word)

    def initUI(self, word):
        # 设置主布局，使用固定的间距
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(10, 10, 10, 10)
        main_layout.setSpacing(15)  # 设置固定间距

        # 第一行：单词标签 - 设置固定高度和自动换行
        self.word_label = QLabel(word)
        self.word_label.setAlignment(Qt.AlignCenter)
        self.word_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.word_label.setMinimumWidth(200)
        self.word_label.setFixedHeight(60)  # 固定高度
        self.word_label.setWordWrap(True)
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.word_label.setFont(font)
        self.word_label.setStyleSheet("""
            QLabel {
                background-color: #f0f0f0;
                padding: 10px;
                border-radius: 5px;
            }
        """)
        self.word_label.mousePressEvent = self.toggle_editors
        main_layout.addWidget(self.word_label)

        # 第二行：含义编辑框
        self.meaning_edit = QTextEdit()
        self.meaning_edit.setPlaceholderText("请输入单词含义")
        self.meaning_edit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.meaning_edit.setMinimumHeight(50)
        self.meaning_edit.setStyleSheet("""
            QTextEdit {
                background-color: #ffffff;
                padding: 8px;
                border: 1px solid #cccccc;
                border-radius: 5px;
            }
        """)
        self.meaning_edit.textChanged.connect(self.adjust_editors_height)
        main_layout.addWidget(self.meaning_edit)

        # 第三行：音标编辑框
        self.pronunciation_edit = QTextEdit()
        self.pronunciation_edit.setPlaceholderText("请输入音标")
        self.pronunciation_edit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.pronunciation_edit.setMinimumHeight(30)
        self.pronunciation_edit.setStyleSheet("""
            QTextEdit {
                background-color: #ffffff;
                padding: 8px;
                border: 1px solid #cccccc;
                border-radius: 5px;
            }
        """)
        self.pronunciation_edit.textChanged.connect(self.adjust_editors_height)
        main_layout.addWidget(self.pronunciation_edit)

        # 初始高度调整
        self.adjust_editors_height()

    def toggle_editors(self, event):
        """切换编辑框的显示和隐藏状态"""
        # 如果当前编辑框是可见的，则隐藏它们
        if self.meaning_edit.isVisible():
            self.meaning_edit.hide()
            self.pronunciation_edit.hide()
        # 否则显示它们
        else:
            self.meaning_edit.show()
            self.pronunciation_edit.show()
        # 调整高度
        self.adjust_editors_height()
        # 传递事件
        super(QLabel, self.word_label).mousePressEvent(event)

    def adjust_editors_height(self):
        """根据内容调整编辑框和整个组件的高度"""
        # 调整含义编辑框高度
        self.adjust_text_edit_height(self.meaning_edit)

        # 调整音标编辑框高度
        self.adjust_text_edit_height(self.pronunciation_edit)

        # 调整整个组件高度
        self.adjust_card_height()

    def adjust_text_edit_height(self, text_edit):
        """根据内容调整单个文本编辑框的高度"""
        if not text_edit.isVisible():
            return

        # 获取文档内容尺寸
        doc = text_edit.document()
        doc_height = doc.size().height()

        # 获取文本编辑框的边距
        contents_margins = text_edit.contentsMargins()
        margins_height = contents_margins.top() + contents_margins.bottom()

        # 计算合适的高度，至少保留最小高度
        min_height = text_edit.minimumHeight()
        new_height = int(doc_height + margins_height + 10)  # 额外增加一些空间
        new_height = max(min_height, new_height)

        # 设置新高度
        text_edit.setFixedHeight(new_height)

    def adjust_card_height(self):
        """根据内容调整整个卡片的高度"""
        # 计算标签的高度 (固定值)
        label_height = self.word_label.height()

        # 计算编辑框的高度，如果隐藏则高度为0
        meaning_height = self.meaning_edit.height() if self.meaning_edit.isVisible() else 0
        pronunciation_height = self.pronunciation_edit.height() if self.pronunciation_edit.isVisible() else 0

        # 计算布局的边距和间距
        margins = self.layout().contentsMargins()
        spacing = self.layout().spacing() * 2  # 两个间距

        # 设置组件的最小高度
        total_height = label_height + meaning_height + pronunciation_height + margins.top() + margins.bottom() + spacing
        self.setMinimumHeight(total_height)
        self.updateGeometry()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # 示例使用
    window = QWidget()
    layout = QVBoxLayout(window)

    card = VocabularyCard("Hello")
    layout.addWidget(card)

    another_card = VocabularyCard("Python")
    another_card.meaning_edit.setText("一种高级编程语言")
    another_card.pronunciation_edit.setText("/ˈpaɪθən/")
    layout.addWidget(another_card)

    window.show()
    sys.exit(app.exec())
