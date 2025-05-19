import sys
from page import MainWindowPage, CustomGrip
from PySide6.QtWidgets import QApplication, QWidget

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindowPage()
    window.show()
    app.exec()
