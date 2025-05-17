from ui import Ui_main_window
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
                               QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
from PySide6.QtCore import Qt, QPropertyAnimation, QEasingCurve, Signal


class MainWindowPage(QWidget, Ui_main_window):
    def __init__(self):
        super().__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setupUi(self)
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
