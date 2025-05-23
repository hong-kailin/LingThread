import sys
from PySide6.QtWidgets import QApplication, QMenu, QWidget, QTextEdit, QVBoxLayout
from PySide6.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建主布局
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)  # 消除边距

        # 创建TextEdit
        self.text_edit = QTextEdit(self)
        self.text_edit.setPlaceholderText("请输入文本...")
        self.text_edit.setContextMenuPolicy(Qt.CustomContextMenu)

        self.text_edit.customContextMenuRequested.connect(self.show_context_menu)
        # 将TextEdit添加到布局
        layout.addWidget(self.text_edit)

        # 设置窗口属性
        self.setWindowTitle('带TextEdit的空白Widget')
        self.setGeometry(300, 300, 500, 400)

    def show_context_menu(self, position):
        # 创建自定义菜单或不创建(即禁用右键菜单)
        menu = QMenu()
        # 添加自定义菜单项
        menu.addAction("自定义操作")
        # 在鼠标位置显示菜单
        menu.exec(self.text_edit.mapToGlobal(position))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())