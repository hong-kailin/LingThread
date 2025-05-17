from PySide6.QtWidgets import QWidget, QApplication
from PySide6.QtCore import Qt, QSequentialAnimationGroup, QPropertyAnimation, QAbstractAnimation, Signal
from ui import Ui_Form
import sys


class RegisterPane(QWidget, Ui_Form):
    exit_signal = Signal()
    register_account_pwd_signal = Signal(str, str)

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setupUi(self)

    def show_hide_menu(self, checked):
        # if checked:
        animation_group = QSequentialAnimationGroup(self)

        animation = QPropertyAnimation()
        animation.setTargetObject(self.about_menu_btn)
        animation.setPropertyName(b"pos")
        animation.setStartValue(self.main_menu_btn.pos())
        animation.setEndValue(self.about_menu_btn.pos())
        animation.setDuration(1000)

        animation_group.addAnimation(animation)
        animation_group.start()

    def about_lk(self):
        print("about_lk")

    def reset(self):
        print("reset")

    def exit(self):
        self.exit_signal.emit()

    def check_register(self):
        self.register_account_pwd_signal.emit(self.account_le.text(), self.password_le.text())

    def enable_register_btn(self):
        account_text = self.account_le.text()
        password_text = self.password_le.text()
        confirm_pwd_text = self.confirm_pwd_le.text()
        if (len(account_text) > 0 and len(password_text) > 0 and len(confirm_pwd_text) > 0
                and password_text == confirm_pwd_text):
            self.register_btn.setEnabled(True)
        else:
            self.register_btn.setEnabled(False)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RegisterPane()
    window.exit_signal.connect(lambda: print("hhhh"))
    window.register_account_pwd_signal.connect(lambda: print("ssss"))
    window.show()
    app.exec()
