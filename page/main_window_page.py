from ui import Ui_main_window
from .custom_grip import CustomEdgeGrip, CustomCornerGrip
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
                               QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
from PySide6.QtCore import Qt, QPropertyAnimation, QEasingCurve, Signal


class MainWindowPage(QWidget, Ui_main_window):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)
        # self.setAttribute(Qt.WA_TranslucentBackground)
        self.setupUi(self)

        self.left_grip = CustomEdgeGrip(self, Qt.LeftEdge)
        self.right_grip = CustomEdgeGrip(self, Qt.RightEdge)
        self.top_grip = CustomEdgeGrip(self, Qt.TopEdge)
        self.bottom_grip = CustomEdgeGrip(self, Qt.BottomEdge)

        self.left_top_grip = CustomCornerGrip(self, "LeftTop")
        self.left_bottom_grip = CustomCornerGrip(self, "LeftBottom")
        self.right_top_grip = CustomCornerGrip(self, "RightTop")
        self.right_bottom_grip = CustomCornerGrip(self, "RightBottom")

        # setting
        self.time_amimation = 500

    def show_hide_btn_name(self, flag):
        if flag:
            width = 60
            widthExtended = 240
        else:
            width = 240
            widthExtended = 60
        self.animation = QPropertyAnimation(self.left_sider_bar, b"minimumWidth")
        self.animation.setDuration(self.time_amimation)
        self.animation.setStartValue(width)
        self.animation.setEndValue(widthExtended)
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()

    def resizeEvent(self, event):
        self.top_grip.setGeometry(10, 0, self.width() - 20, 10)
        self.bottom_grip.setGeometry(10, self.height() - 10, self.width() - 20, 10)
        self.left_grip.setGeometry(0, 10, 10, self.height() - 20)
        self.right_grip.setGeometry(self.width() - 10, 10, 10, self.height() - 20)

        self.left_top_grip.setGeometry(0, 0, 10, 10)
        self.left_bottom_grip.setGeometry(0, self.height() - 10, 10, 10)
        self.right_top_grip.setGeometry(self.width() - 10, 0, 10, 10)
        self.right_bottom_grip.setGeometry(self.width() - 10, self.height() - 10, 10, 10)
