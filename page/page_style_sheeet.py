from ui import Ui_styleSheet
from PySide6.QtWidgets import QWidget


class StyleSheet(QWidget, Ui_styleSheet):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
