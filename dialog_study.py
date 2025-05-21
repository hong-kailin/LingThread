import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QVBoxLayout,
    QDialog, QLabel, QLineEdit, QMessageBox, QWidget
)
from PySide6.QtCore import Qt


class CustomDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        # self.setWindowFlags(Qt.FramelessWindowHint)
        # 设置对话框标题和大小
        self.setWindowTitle("自定义对话框")
        self.setMinimumSize(300, 200)

        # 创建控件
        self.label = QLabel("请输入您的名字:")
        self.name_input = QLineEdit()
        self.submit_button = QPushButton("提交")

        # 设置布局
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.name_input)
        layout.addWidget(self.submit_button)
        self.setLayout(layout)

        # 连接信号与槽
        self.submit_button.clicked.connect(self.accept)  # 点击提交按钮关闭对话框

    def get_name(self):
        return self.name_input.text()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("对话框示例")
        self.setGeometry(100, 100, 400, 300)

        # 创建中央部件和布局
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # 创建按钮
        self.modal_button = QPushButton("显示模态对话框")
        self.modeless_button = QPushButton("显示非模态对话框")
        self.message_button = QPushButton("显示消息框")

        # 添加按钮到布局
        layout.addWidget(self.modal_button)
        layout.addWidget(self.modeless_button)
        layout.addWidget(self.message_button)

        # 连接信号与槽
        self.modal_button.clicked.connect(self.show_modal_dialog)
        self.modeless_button.clicked.connect(self.show_modeless_dialog)
        self.message_button.clicked.connect(self.show_message_box)

        # 存储非模态对话框的引用
        self.modeless_dialog = None

    def show_modal_dialog(self):
        dialog = CustomDialog(self)
        # 以模态方式显示对话框（会阻塞主窗口）
        if dialog.exec():
            print("==")
            name = dialog.get_name()
            if name:
                QMessageBox.information(self, "欢迎", f"你好，{name}！")
            else:
                QMessageBox.warning(self, "警告", "名字不能为空！")

    def show_modeless_dialog(self):
        # 如果对话框已存在则显示，否则创建新的
        if self.modeless_dialog is None:
            self.modeless_dialog = CustomDialog(self)
            # 连接对话框关闭信号到自定义槽函数
            self.modeless_dialog.finished.connect(self.on_modeless_dialog_finished)
        self.modeless_dialog.show()
        # 确保对话框置顶
        self.modeless_dialog.raise_()
        self.modeless_dialog.activateWindow()

    def on_modeless_dialog_finished(self, result):
        if result == QDialog.Accepted:
            name = self.modeless_dialog.get_name()
            if name:
                QMessageBox.information(self, "欢迎", f"你好，{name}！")
            else:
                QMessageBox.warning(self, "警告", "名字不能为空！")

    def show_message_box(self):
        # 显示一个简单的消息框
        result = QMessageBox.question(
            self, "确认", "你确定要执行此操作吗？",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No
        )
        if result == QMessageBox.Yes:
            QMessageBox.information(self, "结果", "你选择了是")
        else:
            QMessageBox.information(self, "结果", "你选择了否")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())