import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QListWidget, QListWidgetItem,
                               QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QLabel)
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QIcon, QPixmap, QColor


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QListWidget 视图模式演示")
        self.resize(600, 400)

        # 创建中心部件和布局
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        # 创建工具栏
        toolbar_layout = QHBoxLayout()

        list_mode_btn = QPushButton("列表模式")
        list_mode_btn.clicked.connect(lambda: self.set_view_mode(QListWidget.ListMode))
        toolbar_layout.addWidget(list_mode_btn)

        icon_mode_btn = QPushButton("图标模式")
        icon_mode_btn.clicked.connect(lambda: self.set_view_mode(QListWidget.IconMode))
        toolbar_layout.addWidget(icon_mode_btn)

        left_to_right_btn = QPushButton("水平布局")
        left_to_right_btn.clicked.connect(lambda: self.set_flow(QListWidget.LeftToRight))
        toolbar_layout.addWidget(left_to_right_btn)

        top_to_bottom_btn = QPushButton("垂直布局")
        top_to_bottom_btn.clicked.connect(lambda: self.set_flow(QListWidget.TopToBottom))
        toolbar_layout.addWidget(top_to_bottom_btn)

        wrapping_btn = QPushButton("启用换行")
        wrapping_btn.setCheckable(True)
        wrapping_btn.toggled.connect(self.toggle_wrapping)
        toolbar_layout.addWidget(wrapping_btn)

        main_layout.addLayout(toolbar_layout)

        # 创建列表控件
        self.list_widget = QListWidget()
        self.list_widget.setSpacing(10)  # 设置项目间距
        self.list_widget.setIconSize(QSize(48, 48))  # 设置图标大小

        # 添加示例项目（使用纯色图标）
        colors = [
            "#FF5733", "#33FF57", "#3357FF", "#FF33F6",
            "#33FFF6", "#FFF633", "#A633FF", "#FFA633",
            "#33FFA6", "#FF3333"
        ]

        names = ["红色", "绿色", "蓝色", "紫色", "青色",
                 "黄色", "靛色", "橙色", "薄荷色", "洋红色"]

        for name, color in zip(names, colors):
            item = QListWidgetItem()
            item.setText(name)

            # 创建纯色图标
            pixmap = QPixmap(48, 48)
            pixmap.fill(QColor(color))
            item.setIcon(QIcon(pixmap))

            self.list_widget.addItem(item)

        main_layout.addWidget(self.list_widget)

        # 状态栏显示当前模式
        self.status_label = QLabel("当前模式: 列表模式, 垂直布局, 禁用换行")
        self.statusBar().addWidget(self.status_label)

        # 设置初始模式
        self.current_view_mode = QListWidget.ListMode
        self.current_flow = QListWidget.TopToBottom
        self.wrapping_enabled = False

    def set_view_mode(self, mode):
        self.current_view_mode = mode
        self.list_widget.setViewMode(mode)
        self.update_status()

    def set_flow(self, flow):
        self.current_flow = flow
        self.list_widget.setFlow(flow)
        self.update_status()

    def toggle_wrapping(self, enabled):
        self.wrapping_enabled = enabled
        self.list_widget.setWrapping(enabled)
        if enabled:
            self.list_widget.setResizeMode(QListWidget.Adjust)  # 启用调整时重新布局
        self.update_status()

    def update_status(self):
        mode_text = "列表模式" if self.current_view_mode == QListWidget.ListMode else "图标模式"
        flow_text = "水平布局" if self.current_flow == QListWidget.LeftToRight else "垂直布局"
        wrap_text = "启用换行" if self.wrapping_enabled else "禁用换行"

        self.status_label.setText(f"当前模式: {mode_text}, {flow_text}, {wrap_text}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())