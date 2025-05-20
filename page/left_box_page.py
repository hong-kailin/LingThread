from PySide6.QtCore import Qt, QPropertyAnimation, QEasingCurve, Signal, QEvent, QTimer
from PySide6.QtGui import QCursor
from PySide6.QtWidgets import QWidget
from ui import Ui_left_box


class LeftBoxPage(QWidget, Ui_left_box):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
