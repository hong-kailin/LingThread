import sys
import os

from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QFileDialog
from PySide6.QtCore import Qt
from PySide6.QtGui import QAction, QShortcut, QKeySequence

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.exec()
