from PySide6.QtCore import Qt, QPropertyAnimation, Signal, QEasingCurve, Signal, QEvent, QTimer
from PySide6.QtGui import QCursor
from PySide6.QtWidgets import QWidget
from ui import Ui_left_box


class LeftBoxPage(QWidget, Ui_left_box):
    show_hide_left_box_signal = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

    def close_left_box(self):
        self.show_hide_left_box_signal.emit()
