from datetime import datetime
from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QDialog, QFileDialog, QLabel, QMessageBox
from PySide6.QtGui import QPixmap
from ui import Ui_new_dialog


class NewDialogPage(QDialog, Ui_new_dialog):
    create_new_project_signal = Signal(str, str, str, str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint | Qt.Dialog)

        self.image_path = None
        self.name = None
        self.author = None
        self.time_labe_str = None
        self.set_function()

    def set_function(self):
        self.cover_label.mousePressEvent = self.select_image

        self.time_labe_str = "Creat Time: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.time_label.setText(self.time_labe_str)
        self.time_label.setAlignment(Qt.AlignRight | Qt.AlignBottom)

    def select_image(self, event):
        """选择图片文件"""
        path, _ = QFileDialog.getOpenFileName(
            self,
            "选择项目图片",
            "",
            "图片文件 (*.png *.jpg *.jpeg)"
        )
        if path:
            self.image_path = path
            pixmap = QPixmap(path)
            pixmap = pixmap.scaled(200, 300, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.cover_label.setPixmap(pixmap)
            self.cover_label.setAlignment(Qt.AlignCenter)

    def create_new_project(self):
        self.name = self.name_edit.text()
        self.author = self.author_edit.text()
        if self.image_path and self.name and self.author:
            self.create_new_project_signal.emit(self.image_path, self.name, self.author, self.time_labe_str)
            self.accept()
        else:
            QMessageBox.warning(self, "警告", "名字不能为空！")
