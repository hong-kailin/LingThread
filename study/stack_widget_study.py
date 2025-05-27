import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QPushButton,
                               QVBoxLayout, QHBoxLayout, QStackedWidget, QLabel)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Widget切换示例")
        self.resize(400, 300)

        # 创建中心部件和主布局
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        # 创建按钮布局
        button_layout = QHBoxLayout()

        # 创建切换按钮
        btn_widget1 = QPushButton("显示Widget 1")
        btn_widget2 = QPushButton("显示Widget 2")
        btn_widget1.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(0))
        btn_widget2.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(1))

        button_layout.addWidget(btn_widget1)
        button_layout.addWidget(btn_widget2)

        # 创建堆叠控件
        self.stacked_widget = QStackedWidget()

        # 创建两个示例widget
        widget1 = QWidget()
        layout1 = QVBoxLayout(widget1)
        layout1.addWidget(QLabel("这是Widget 1"))
        layout1.addWidget(QPushButton("Widget 1 中的按钮"))

        widget2 = QWidget()
        layout2 = QVBoxLayout(widget2)
        layout2.addWidget(QLabel("这是Widget 2"))
        layout2.addWidget(QPushButton("Widget 2 中的按钮"))

        # 将widget添加到堆叠控件
        self.stacked_widget.addWidget(widget1)
        self.stacked_widget.addWidget(widget2)

        # 将按钮布局和堆叠控件添加到主布局
        main_layout.addLayout(button_layout)
        main_layout.addWidget(self.stacked_widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())