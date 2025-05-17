from PySide6.QtWidgets import QWidget, QApplication
from PySide6.QtCore import Qt, Signal
from ui import Ui_Login_Form
import sys


class LoginPane(QWidget, Ui_Login_Form):
    show_register_pane_signal = Signal()

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setupUi(self)

    def show_register_pane(self):
        self.show_register_pane_signal.emit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginPane()
    window.show()
    app.exec()
