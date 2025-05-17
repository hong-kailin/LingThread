import sys
from datetime import datetime
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QFileDialog
)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt


class ProjectCreator(QWidget):
    def __init__(self):
        super().__init__()
        self.image_path = ""  # 存储用户选择的图片路径
        self.initUI()

    def initUI(self):
        # 设置窗口属性
        self.setWindowTitle('新建项目')
        self.setGeometry(300, 300, 600, 400)

        # 主布局（水平排列：左侧图片 + 右侧表单）
        main_layout = QHBoxLayout()

        # 左侧图片区域
        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setFixedSize(250, 250)
        self.image_label.setText("点击选择图片\n(推荐尺寸 250x250)")
        self.image_label.setStyleSheet("border: 2px dashed #aaa;")
        self.image_label.mousePressEvent = self.select_image  # 绑定点击事件

        # 右侧表单区域
        form_layout = QVBoxLayout()

        # 项目名称输入
        name_layout = QVBoxLayout()
        name_layout.addWidget(QLabel("项目名称:"))
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("请输入项目名称")
        name_layout.addWidget(self.name_input)

        # 作者输入
        author_layout = QVBoxLayout()
        author_layout.addWidget(QLabel("项目作者:"))
        self.author_input = QLineEdit()
        self.author_input.setPlaceholderText("请输入作者名称")
        author_layout.addWidget(self.author_input)

        # 自动生成日期
        date_layout = QVBoxLayout()
        date_layout.addWidget(QLabel("创建日期:"))
        self.date_label = QLabel(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        self.date_label.setStyleSheet("color: #666;")
        date_layout.addWidget(self.date_label)

        # 按钮区域
        button_layout = QHBoxLayout()
        self.create_btn = QPushButton("创建")
        self.create_btn.clicked.connect(self.create_project)
        self.cancel_btn = QPushButton("取消")
        self.cancel_btn.clicked.connect(self.close)
        button_layout.addWidget(self.create_btn)
        button_layout.addWidget(self.cancel_btn)

        # 将表单元素添加到右侧布局
        form_layout.addLayout(name_layout)
        form_layout.addLayout(author_layout)
        form_layout.addLayout(date_layout)
        form_layout.addStretch()  # 添加弹性空间
        form_layout.addLayout(button_layout)

        # 将左右部分添加到主布局
        main_layout.addWidget(self.image_label)
        main_layout.addLayout(form_layout)

        self.setLayout(main_layout)

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
            # 加载并显示图片
            pixmap = QPixmap(path)
            pixmap = pixmap.scaled(250, 250, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.image_label.setPixmap(pixmap)
            self.image_label.setAlignment(Qt.AlignCenter)

    def create_project(self):
        """创建项目按钮点击事件"""
        project_data = {
            "name": self.name_input.text(),
            "author": self.author_input.text(),
            "date": self.date_label.text(),
            "image": self.image_path
        }
        # 这里可以添加实际创建项目的逻辑
        print("创建项目参数:", project_data)
        # self.close()  # 根据需求决定是否关闭窗口


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ProjectCreator()
    window.show()
    sys.exit(app.exec())