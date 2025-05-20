import sys
from page import MainWindowPage, LeftBoxPage
from PySide6.QtWidgets import QApplication, QWidget

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindowPage()
    left_box = LeftBoxPage(window.left_hide_box)

    # window.show_hide_left_box_signal.connect(left_box.show_hide)

    window.show()
    app.exec()
