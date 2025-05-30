from PySide6.QtCore import (Qt, QPropertyAnimation, Signal,
                            QEasingCurve, Signal, QEvent, QTimer)
from PySide6.QtGui import QCursor, QTextCursor, QTextCharFormat, QColor
from PySide6.QtWidgets import QWidget, QMenu, QTextEdit
from ui import Ui_container


class ContainerWidgetPage(QWidget, Ui_container):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

    def scroll_to_card(self, card):
        if card and card.isVisible():
            card_rect = card.geometry()
            scroll_pos = card_rect.top() - 5
            self.scrollArea.verticalScrollBar().setValue(scroll_pos)

