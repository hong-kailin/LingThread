from ui import Ui_ai_chat_widget
from PySide6.QtCore import (Qt, QPropertyAnimation, Signal,
                            QEasingCurve, Signal, QEvent, QTimer)
from PySide6.QtGui import QCursor, QTextCursor, QTextCharFormat, QColor
from PySide6.QtWidgets import QWidget


class AiChatWidgetPage(QWidget, Ui_ai_chat_widget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
