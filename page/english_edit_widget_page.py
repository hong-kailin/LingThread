from PySide6.QtCore import Qt, QPropertyAnimation, Signal, QEasingCurve, Signal, QEvent, QTimer
from PySide6.QtGui import QCursor
from PySide6.QtWidgets import QWidget
from ui import Ui_english_edit_widget


class EnglishEditWidgetPage(QWidget, Ui_english_edit_widget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
