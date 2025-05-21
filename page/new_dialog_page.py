from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog
from ui import Ui_new_dialog


class NewDialogPage(QDialog, Ui_new_dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(self.windowFlags()|Qt.FramelessWindowHint|Qt.Dialog)
