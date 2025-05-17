import sys
from page import MainWindowPage
from PySide6.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindowPage()
    window.show()
    app.exec()
