import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                               QHBoxLayout, QScrollArea, QLabel, QSplitter,
                               QPushButton, QFrame, QTextEdit)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置窗口标题和尺寸
        self.setWindowTitle("双滚动区域分割界面")
        self.setGeometry(300, 300, 1000, 600)

        # 创建主部件和主布局
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        # 创建顶部标题
        title_label = QLabel("双滚动区域示例")
        title_label.setAlignment(Qt.AlignCenter)
        title_font = QFont("SimHei", 16, QFont.Bold)
        title_label.setFont(title_font)
        main_layout.addWidget(title_label)

        # 创建水平分割器
        splitter = QSplitter(Qt.Horizontal)

        # 创建左侧滚动区域
        left_scroll_area = QScrollArea()
        left_scroll_area.setWidgetResizable(True)
        left_scroll_area.setStyleSheet("""
            QScrollArea {
                border: 1px solid #ddd;
                border-radius: 4px;
                background-color: #f9f9f9;
            }
            QScrollBar:vertical {
                width: 10px;
                background: #f0f0f0;
            }
            QScrollBar::handle:vertical {
                background: #ccc;
                border-radius: 5px;
            }
        """)

        # 左侧滚动区域内容
        left_content = QWidget()
        left_layout = QVBoxLayout(left_content)

        # 添加一些示例内容到左侧
        for i in range(20):
            btn = QPushButton(f"左侧按钮 {i + 1}")
            btn.setFixedHeight(30)
            left_layout.addWidget(btn)

        left_layout.addStretch()
        left_scroll_area.setWidget(left_content)

        # 创建右侧滚动区域
        right_scroll_area = QScrollArea()
        right_scroll_area.setWidgetResizable(True)
        right_scroll_area.setStyleSheet("""
            QScrollArea {
                border: 1px solid #ddd;
                border-radius: 4px;
                background-color: #f9f9f9;
            }
            QScrollBar:vertical {
                width: 10px;
                background: #f0f0f0;
            }
            QScrollBar::handle:vertical {
                background: #ccc;
                border-radius: 5px;
            }
        """)

        # 右侧滚动区域内容
        right_content = QWidget()
        right_layout = QVBoxLayout(right_content)

        # 添加文本编辑框到右侧
        text_edit = QTextEdit()
        text_edit.setPlaceholderText("在这里输入一些文本...")
        text_edit.setStyleSheet("""
            QTextEdit {
                border: 1px solid #ddd;
                border-radius: 4px;
                padding: 8px;
                font-size: 14px;
            }
        """)
        right_layout.addWidget(text_edit)

        # 添加一些示例内容到右侧
        for i in range(10):
            label = QLabel(f"右侧内容行 {i + 1}")
            label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
            label.setFixedHeight(30)
            right_layout.addWidget(label)

        right_layout.addStretch()
        right_scroll_area.setWidget(right_content)

        # 将两个滚动区域添加到分割器
        splitter.addWidget(left_scroll_area)
        splitter.addWidget(right_scroll_area)

        # 设置分割器初始大小比例
        splitter.setSizes([400, 600])

        # 设置分割器样式
        splitter.setStyleSheet("""
            QSplitter::handle {
                background-color: #ddd;
                width: 5px;
                border-radius: 2px;
            }
            QSplitter::handle:hover {
                background-color: #aaa;
            }
        """)

        # 将分割器添加到主布局
        main_layout.addWidget(splitter)

        # 创建底部状态栏
        status_bar = self.statusBar()
        status_bar.showMessage("就绪")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 设置应用全局字体以确保中文正常显示
    font = QFont("SimHei")
    app.setFont(font)

    window = MainWindow()
    window.show()
    sys.exit(app.exec())