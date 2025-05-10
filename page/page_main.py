from ui import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow, QVBoxLayout
from .page_style_sheeet import StyleSheet


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.style_sheet = StyleSheet()
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.style_sheet)
        self.styleSheet.setLayout(layout)
