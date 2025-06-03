import sys
import os
from PySide6.QtWidgets import QApplication, QVBoxLayout
from page import (MainWindowPage, LeftBoxPage, NewDialogPage, ProjectWidgetListPage)
from database import Project


class LingThread:
    def __init__(self):
        self.data_save_path = "./data"
        self.main_window = MainWindowPage()
        self.setup_ui()

    def setup_ui(self):
        v_layout = QVBoxLayout(self.main_window.left_hide_box)
        v_layout.setContentsMargins(0, 0, 0, 0)
        left_box = LeftBoxPage()
        v_layout.addWidget(left_box)
        left_box.show_hide_left_box_signal.connect(self.main_window.show_hide_left_box)

        v_layout_2 = QVBoxLayout(self.main_window.project_list_page)
        v_layout_2.setContentsMargins(0, 0, 0, 0)
        self.project_widget_list = ProjectWidgetListPage(self.main_window.project_list_page)
        v_layout_2.addWidget(self.project_widget_list)
        self.main_window.stacked_widget.setCurrentIndex(2)
        self.main_window.create_new_project_signal.connect(self.create_new_project)

    def show(self):
        self.main_window.show()

    def create_new_project(self):
        new_window = NewDialogPage(self.main_window)

        def _create_new_project(image_path, name, author, modified_time):
            project = Project(name, author, modified_time, image_path, self.data_save_path)
            self.project_widget_list.add_new_project(project)

        new_window.create_new_project_signal.connect(_create_new_project)
        if new_window.exec():
            return


if __name__ == "__main__":
    app = QApplication(sys.argv)
    LT = LingThread()
    LT.show()
    app.exec()
