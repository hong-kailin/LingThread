import sys
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import Qt
from custom_grip import CustomGrip


class FramelessWindow(QWidget):
    def __init__(self):
        super().__init__()

        # 窗口设置
        self.setWindowTitle("Custom Grip Example")
        self.resize(400, 300)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.content = QWidget(self)
        self.content.setStyleSheet("background: #2c313c;")
        self.content.setGeometry(0, 0, 400, 300)

        # 下面的代码一定写到self.content = QWidget(self)后面
        self.top_grip = CustomGrip(self, Qt.TopEdge, disable_color=False)
        self.bottom_grip = CustomGrip(self, Qt.BottomEdge, disable_color=False)
        self.left_grip = CustomGrip(self, Qt.LeftEdge, disable_color=False)
        self.right_grip = CustomGrip(self, Qt.RightEdge, disable_color=False)

    def resizeEvent(self, event):
        """更新手柄位置"""
        self.top_grip.setGeometry(0, 0, self.width(), 10)
        self.bottom_grip.setGeometry(0, self.height() - 10, self.width(), 10)
        self.left_grip.setGeometry(0, 10, 10, self.height() - 10)
        self.right_grip.setGeometry(self.width() - 10, 10, 10, self.height() - 10)
        self.content.setGeometry(0, 0, self.width(), self.height())

    def mousePressEvent(self, event):
        """实现窗口拖动功能"""
        if event.button() == Qt.LeftButton:
            self.drag_start = event.globalPosition().toPoint()
            self.original_geometry = self.geometry()
            event.accept()

    def mouseMoveEvent(self, event):
        """窗口拖动逻辑"""
        if hasattr(self, 'drag_start'):
            delta = event.globalPosition().toPoint() - self.drag_start
            new_x = self.original_geometry.x() + delta.x()
            new_y = self.original_geometry.y() + delta.y()
            self.move(new_x, new_y)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FramelessWindow()
    window.show()
    sys.exit(app.exec())
