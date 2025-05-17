from PySide6.QtWidgets import QWidget, QApplication
import sys
from login_pane import LoginPane
from register_pane import RegisterPane

if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_pane_ = LoginPane()


    def show_register_pane():
        register_pane_ = RegisterPane(login_pane_)  # 即使被析构了，也会因为父对象存在而一直存在
        register_pane_.move(100, 100)
        register_pane_.show()


    login_pane_.show_register_pane_signal.connect(show_register_pane)

    login_pane_.show()
    app.exec_()
