import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QTextEdit,
    QVBoxLayout, QSizePolicy
)
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QFont, QTextCursor


class VocabularyWidget(QWidget):
    def __init__(self, word="hello"):
        super().__init__()
        self.initUI(word)

    def initUI(self, word):
        # 设置窗口基本属性
        self.setWindowTitle('单词学习工具')
        self.setMinimumWidth(400)

        # 创建主布局
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(10, 10, 10, 10)
        main_layout.setSpacing(10)

        # 第一行：单词显示标签
        self.word_label = QLabel(word)
        self.word_label.setAlignment(Qt.AlignCenter)
        self.word_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
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
        self.word_label.setCursor(Qt.PointingHandCursor)
        self.word_label.mousePressEvent = self.toggle_inputs  # 设置点击事件
        main_layout.addWidget(self.word_label)

        # 第二行：含义输入框
        self.meaning_input = QTextEdit()
        self.meaning_input.setPlaceholderText("请输入单词含义")
        self.meaning_input.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.meaning_input.setMinimumHeight(60)
        self.meaning_input.textChanged.connect(self.adjust_text_edit_height)
        main_layout.addWidget(self.meaning_input)

        # 第三行：音标输入框
        self.pronunciation_input = QTextEdit()
        self.pronunciation_input.setPlaceholderText("请输入音标")
        self.pronunciation_input.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.pronunciation_input.setMinimumHeight(40)
        self.pronunciation_input.textChanged.connect(self.adjust_text_edit_height)
        main_layout.addWidget(self.pronunciation_input)

        # 初始状态：显示输入框
        self.inputs_visible = True

        # 调整初始高度
        self.adjust_text_edit_height()

    def toggle_inputs(self, event):
        """切换输入框的显示和隐藏状态"""
        self.inputs_visible = not self.inputs_visible
        self.meaning_input.setVisible(self.inputs_visible)
        self.pronunciation_input.setVisible(self.inputs_visible)
        self.adjustSize()  # 调整窗口大小

    def adjust_text_edit_height(self):
        """根据文本内容调整QTextEdit的高度"""
        for text_edit in [self.meaning_input, self.pronunciation_input]:
            if text_edit.isVisible():
                # 获取文档的理想高度
                doc_height = text_edit.document().size().height()
                # 考虑到边距和滚动条
                new_height = doc_height + text_edit.contentsMargins().top() + text_edit.contentsMargins().bottom() + 10
                # 设置最小高度和最大高度相同，强制使用这个高度
                text_edit.setMinimumHeight(new_height)
                text_edit.setMaximumHeight(new_height)
        # 调整整个窗口的大小
        self.adjustSize()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = VocabularyWidget("hello")
    window.show()
    sys.exit(app.exec())