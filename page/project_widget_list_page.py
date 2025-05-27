from ui import Ui_project_list
from PySide6.QtWidgets import (QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
from PySide6.QtCore import QEvent


class ProjectWidgetListPage(QWidget, Ui_project_list):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
