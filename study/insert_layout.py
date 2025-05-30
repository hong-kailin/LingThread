import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QScrollArea,
                               QWidget, QVBoxLayout, QLabel, QPushButton, QFrame)
from PySide6.QtCore import Qt
from PySide6.QtGui import QPalette, QColor


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ScrollArea 透明区域示例")
        self.setGeometry(100, 100, 600, 400)

        # 创建滚动区域
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        # 创建滚动区域的内容部件
        content_widget = QWidget()
        self.layout = QVBoxLayout(content_widget)
        self.layout.setAlignment(Qt.AlignTop)

        # 添加一些示例内容
        for i in range(5):
            label = QLabel(f"这是第 {i + 1} 个标签")
            label.setAlignment(Qt.AlignCenter)
            label.setMinimumHeight(50)
            label.setStyleSheet("background-color: lightblue; border-radius: 5px;")
            self.layout.addWidget(label)

        # 添加按钮用于测试添加widget
        add_button = QPushButton("在透明区域前添加Widget")
        add_button.clicked.connect(self.add_widget)
        self.layout.addWidget(add_button)

        # 添加空白透明区域(放在最后)
        self.transparent_space = QWidget()
        self.transparent_space.setMinimumHeight(500)  # 设置透明区域高度
        # 设置为透明背景
        self.transparent_space.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.layout.addWidget(self.transparent_space)

        # 将内容部件设置到滚动区域
        scroll_area.setWidget(content_widget)
        self.setCentralWidget(scroll_area)

    def add_widget(self):
        # 在透明区域前添加新widget
        new_widget = QLabel("新添加的Widget")
        new_widget.setAlignment(Qt.AlignCenter)
        new_widget.setMinimumHeight(50)
        new_widget.setStyleSheet("background-color: lightgreen; border-radius: 5px;")

        # 计算插入位置(透明区域前一个位置)
        insert_position = self.layout.count() - 1
        self.layout.insertWidget(insert_position, new_widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())