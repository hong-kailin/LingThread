from PySide6.QtCore import Qt, QPropertyAnimation, Signal, QEasingCurve, Signal, QEvent, QTimer
from PySide6.QtGui import QCursor
from PySide6.QtWidgets import QWidget, QMenu
from ui import Ui_english_edit_widget


class EnglishEditWidgetPage(QWidget, Ui_english_edit_widget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.english_edit.setContextMenuPolicy(Qt.CustomContextMenu)

    def show_text_menu(self, pos):
        cursor = self.english_edit.textCursor()
        if cursor.hasSelection():
            menu = QMenu(self)
            create_action = menu.addAction("创建卡片")
            # create_action.triggered.connect(lambda: self.create_card(cursor))
            menu.exec_(self.english_edit.mapToGlobal(pos))
