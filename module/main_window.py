from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtCore import Qt
from page import MainWindowPage, LeftBoxPage, NewDialogPage


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()
        self.main_window.setWindowFlags(Qt.FramelessWindowHint)
        # self.setAttribute(Qt.WA_TranslucentBackground)

    def setup_ui(self):
        self.main_window = MainWindowPage()
        v_layout = QVBoxLayout(self.main_window.left_hide_box)
        v_layout.setContentsMargins(0, 0, 0, 0)
        left_box = LeftBoxPage()
        v_layout.addWidget(left_box)
        left_box.show_hide_left_box_signal.connect(self.main_window.show_hide_left_box)

    def show(self):
        self.main_window.show()

    def create_new_project(self):
        new_window = NewDialogPage(self.main_window)
        new_window.create_new_project_signal.connect(self.add_new_project)
        if new_window.exec():
            return
