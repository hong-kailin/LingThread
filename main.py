import sys
import os

from PySide6.QtWidgets import QApplication
from module import MainWindow


class LingThread:
    def __init__(self):
        self.setup_ui()

    def setup_ui(self):
        self.main_window = MainWindow()

    def show(self):
        self.main_window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    LT = LingThread()
    LT.show()
    app.exec()
