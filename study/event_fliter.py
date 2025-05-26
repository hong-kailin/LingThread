import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTextEdit, QLabel, QVBoxLayout, QWidget
from PySide6.QtCore import Qt, QEvent


class EventFilterExample(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建中央部件和布局
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)
        self.setCentralWidget(central_widget)

        # 创建一个标签用于显示事件信息
        self.event_label = QLabel("事件信息将显示在这里")
        layout.addWidget(self.event_label)

        # 创建文本编辑框
        self.text_edit = QTextEdit()
        self.text_edit.setPlaceholderText("点击或输入文本...")
        layout.addWidget(self.text_edit)

        # 为文本编辑框安装事件过滤器
        self.text_edit.installEventFilter(self)

        self.setWindowTitle("事件过滤器示例")
        self.setGeometry(300, 300, 600, 400)

    def eventFilter(self, obj, event):
        # 检查事件来源是否为文本编辑框
        if obj == self.text_edit:
            # 处理鼠标按下事件
            if event.type() == QEvent.MouseButtonPress:
                self.event_label.setText("检测到鼠标点击文本编辑框")
                # 返回True表示拦截事件，不再继续处理
                # 返回False表示继续传递事件给原对象
                return False

            # 处理键盘按下事件
            elif event.type() == QEvent.KeyPress:
                self.event_label.setText(f"按下了键: {event.text()}")
                return False

            # 处理焦点事件
            elif event.type() == QEvent.FocusIn:
                self.event_label.setText("文本编辑框获得焦点")
                return False

            elif event.type() == QEvent.FocusOut:
                self.event_label.setText("文本编辑框失去焦点")
                return False

        # 其他事件继续传递
        return super().eventFilter(obj, event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = EventFilterExample()
    window.show()
    sys.exit(app.exec())