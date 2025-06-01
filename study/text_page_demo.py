import sys
import random
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                               QHBoxLayout, QTextEdit, QPushButton, QLabel,
                               QLineEdit, QMessageBox)
from PySide6.QtCore import Qt


class TextPaginationApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("文本分页显示应用")
        self.setGeometry(100, 100, 800, 600)

        # 创建中心部件和布局
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)

        # 创建文本显示区域
        self.text_display = QTextEdit()
        self.text_display.setReadOnly(True)
        self.main_layout.addWidget(self.text_display)

        # 创建分页控制区域
        self.pagination_layout = QHBoxLayout()

        # 上一页按钮
        self.prev_button = QPushButton("上一页")
        self.prev_button.clicked.connect(self.prev_page)
        self.pagination_layout.addWidget(self.prev_button)

        # 当前页码和总页数标签
        self.page_label = QLabel("第 1 页，共 10 页")
        self.pagination_layout.addWidget(self.page_label, alignment=Qt.AlignCenter)

        # 下一页按钮
        self.next_button = QPushButton("下一页")
        self.next_button.clicked.connect(self.next_page)
        self.pagination_layout.addWidget(self.next_button)

        # 跳转到指定页
        self.page_jump_layout = QHBoxLayout()
        self.page_jump_layout.addWidget(QLabel("转到第"))

        self.page_input = QLineEdit()
        self.page_input.setMaximumWidth(50)
        self.page_input.setAlignment(Qt.AlignCenter)
        self.page_input.returnPressed.connect(self.jump_to_page)
        self.page_jump_layout.addWidget(self.page_input)

        self.page_jump_layout.addWidget(QLabel("页"))
        self.go_button = QPushButton("前往")
        self.go_button.clicked.connect(self.jump_to_page)
        self.page_jump_layout.addWidget(self.go_button)

        self.pagination_layout.addLayout(self.page_jump_layout)

        self.main_layout.addLayout(self.pagination_layout)

        # 初始化页码和文本数据
        self.current_page = 1
        self.total_pages = 10
        self.text_data = self.generate_sample_text()
        self.update_display()

    def generate_sample_text(self):
        """生成示例文本数据，返回包含10页文本的列表"""
        paragraphs = []
        lorem_ipsum = (
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt "
            "ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco "
            "laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in "
            "voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat "
            "non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
        )

        # 生成10页文本，每页3段
        for _ in range(self.total_pages):
            page_text = ""
            for _ in range(3):
                # 随机调整段落长度
                repeat = random.randint(1, 3)
                page_text += (lorem_ipsum * repeat) + "\n\n"
            paragraphs.append(page_text)

        return paragraphs

    def update_display(self):
        """更新文本显示和页码标签"""
        # 更新文本显示
        self.text_display.setText(self.text_data[self.current_page - 1])

        # 更新页码标签
        self.page_label.setText(f"第 {self.current_page} 页，共 {self.total_pages} 页")

        # 禁用/启用按钮
        self.prev_button.setEnabled(self.current_page > 1)
        self.next_button.setEnabled(self.current_page < self.total_pages)

        # 清空并聚焦到页码输入框
        self.page_input.clear()

    def prev_page(self):
        """切换到上一页"""
        if self.current_page > 1:
            self.current_page -= 1
            self.update_display()

    def next_page(self):
        """切换到下一页"""
        if self.current_page < self.total_pages:
            self.current_page += 1
            self.update_display()

    def jump_to_page(self):
        """跳转到指定页码"""
        try:
            page_num = int(self.page_input.text())
            if 1 <= page_num <= self.total_pages:
                self.current_page = page_num
                self.update_display()
            else:
                QMessageBox.warning(self, "页码错误", f"请输入1到{self.total_pages}之间的页码")
        except ValueError:
            QMessageBox.warning(self, "输入错误", "请输入有效的页码数字")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TextPaginationApp()
    window.show()
    sys.exit(app.exec())