from PySide6.QtCore import (Qt, QPropertyAnimation, Signal,
                            QEasingCurve, Signal, QEvent, QTimer)
from PySide6.QtGui import QCursor, QTextCursor, QTextCharFormat, QColor
from PySide6.QtWidgets import QWidget, QMenu, QTextEdit
from ui import Ui_container


class ContainerWidgetPage(QWidget, Ui_container):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
