import sys
from datetime import datetime
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QListWidget, QListWidgetItem, QGridLayout,
    QSplitter, QFrame, QSizePolicy
)
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QPixmap, QColor, QPalette, QFont


class Project:
    def __init__(self, name, author, modified_date, color="#CCCCCC"):
        self.name = name
        self.author = author
        self.modified_date = modified_date
        self.color = color


class ProjectListItem(QWidget):
    def __init__(self, project, parent=None):
        super().__init__(parent)
        self.setup_ui(project)

    def setup_ui(self, project):
        layout = QHBoxLayout(self)
        layout.setContentsMargins(5, 5, 5, 5)
        layout.setSpacing(10)

        # 封面图片
        cover_label = QLabel()
        cover_label.setFixedSize(80, 60)
        cover_label.setAutoFillBackground(True)
        palette = cover_label.palette()
        palette.setColor(QPalette.Window, QColor(project.color))
        cover_label.setPalette(palette)
        layout.addWidget(cover_label)

        # 项目名称
        name_label = QLabel(project.name)
        font = name_label.font()
        font.setBold(True)
        name_label.setFont(font)
        name_label.setFixedWidth(150)
        name_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        layout.addWidget(name_label)

        # 作者
        author_label = QLabel(project.author)
        author_label.setFixedWidth(100)
        author_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        layout.addWidget(author_label)

        # 修改时间
        date_label = QLabel(project.modified_date)
        date_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        layout.addWidget(date_label, 1)


class ProjectGridItem(QWidget):
    def __init__(self, project, parent=None):
        super().__init__(parent)
        self.setup_ui(project)

    def setup_ui(self, project):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(5, 5, 5, 5)
        layout.setSpacing(5)

        # 封面图片
        cover_label = QLabel()
        cover_label.setFixedSize(120, 90)
        cover_label.setAutoFillBackground(True)
        palette = cover_label.palette()
        palette.setColor(QPalette.Window, QColor(project.color))
        cover_label.setPalette(palette)
        layout.addWidget(cover_label, alignment=Qt.AlignCenter)

        # 项目名称
        name_label = QLabel(project.name)
        name_label.setAlignment(Qt.AlignCenter)
        font = name_label.font()
        font.setBold(True)
        name_label.setFont(font)
        name_label.setWordWrap(True)
        layout.addWidget(name_label)

        # 作者
        author_label = QLabel(f"作者: {project.author}")
        author_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(author_label)

        # 修改时间
        date_label = QLabel(f"{project.modified_date}")
        date_label.setAlignment(Qt.AlignCenter)
        date_label.setStyleSheet("color: #666666; font-size: 10pt;")
        layout.addWidget(date_label)


class ProjectListView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("项目列表查看器")
        self.resize(800, 600)

        self.projects = self.create_sample_projects()
        self.current_view_mode = "list"  # 初始视图模式为列表

        self.setup_ui()

    def setup_ui(self):
        # 主布局
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        # 工具栏
        toolbar_layout = QHBoxLayout()
        toolbar_layout.setContentsMargins(0, 0, 0, 0)

        list_view_button = QPushButton("列表视图")
        list_view_button.clicked.connect(lambda: self.change_view_mode("list"))
        toolbar_layout.addWidget(list_view_button)

        grid_view_button = QPushButton("网格视图")
        grid_view_button.clicked.connect(lambda: self.change_view_mode("grid"))
        toolbar_layout.addWidget(grid_view_button)

        toolbar_layout.addStretch()

        main_layout.addLayout(toolbar_layout)

        # 分割器
        splitter = QSplitter(Qt.Vertical)

        # 项目列表区域
        self.list_widget = QListWidget()
        self.list_widget.setSpacing(5)
        self.list_widget.setUniformItemSizes(True)
        self.update_project_list()

        splitter.addWidget(self.list_widget)

        # 状态栏
        status_label = QLabel(f"共 {len(self.projects)} 个项目")
        self.statusBar().addWidget(status_label)

        main_layout.addWidget(splitter)

    def create_sample_projects(self):
        # 创建示例项目数据
        return [
            Project("网站设计项目", "张三", "2023-05-15", "#FF9999"),
            Project("移动应用开发", "李四", "2023-05-14", "#99FF99"),
            Project("数据分析报告", "王五", "2023-05-13", "#9999FF"),
            Project("UI/UX设计稿", "赵六", "2023-05-12", "#FFFF99"),
            Project("市场营销策划", "钱七", "2023-05-11", "#FF99FF"),
            Project("游戏开发", "孙八", "2023-05-10", "#99FFFF"),
            Project("人工智能项目", "周九", "2023-05-09", "#FFCC99"),
            Project("电商平台优化", "吴十", "2023-05-08", "#CCFF99"),
            Project("企业管理系统", "郑十一", "2023-05-07", "#99CCFF"),
            Project("微信小程序", "王十二", "2023-05-06", "#FF99CC")
        ]

    def update_project_list(self):
        self.list_widget.clear()

        if self.current_view_mode == "list":
            self.list_widget.setViewMode(QListWidget.ListMode)
            self.list_widget.setFlow(QListWidget.TopToBottom)
            self.list_widget.setIconSize(QSize(80, 60))

            # 添加表头
            header_item = QListWidgetItem()
            header_item.setSizeHint(QSize(0, 30))
            self.list_widget.addItem(header_item)

            header_widget = QWidget()
            header_layout = QHBoxLayout(header_widget)
            header_layout.setContentsMargins(5, 5, 5, 5)
            header_layout.setSpacing(10)

            header_cover = QLabel("封面")
            header_cover.setFixedSize(80, 20)
            header_layout.addWidget(header_cover)

            header_name = QLabel("项目名称")
            header_name.setFixedWidth(150)
            font = header_name.font()
            font.setBold(True)
            header_name.setFont(font)
            header_layout.addWidget(header_name)

            header_author = QLabel("作者")
            header_author.setFixedWidth(100)
            font = header_author.font()
            font.setBold(True)
            header_author.setFont(font)
            header_layout.addWidget(header_author)

            header_date = QLabel("修改时间")
            font = header_date.font()
            font.setBold(True)
            header_date.setFont(font)
            header_layout.addWidget(header_date, 1)

            header_widget.setStyleSheet("background-color: #E0E0E0;")
            self.list_widget.setItemWidget(header_item, header_widget)

            # 添加分割线
            line_item = QListWidgetItem()
            line_item.setSizeHint(QSize(0, 2))
            self.list_widget.addItem(line_item)

            line_widget = QFrame()
            line_widget.setFrameShape(QFrame.HLine)
            line_widget.setFrameShadow(QFrame.Sunken)
            self.list_widget.setItemWidget(line_item, line_widget)

            # 添加项目
            for project in self.projects:
                item = QListWidgetItem()
                item.setSizeHint(QSize(0, 70))
                self.list_widget.addItem(item)

                widget = ProjectListItem(project)
                self.list_widget.setItemWidget(item, widget)
        else:  # 网格视图
            self.list_widget.setViewMode(QListWidget.IconMode)
            self.list_widget.setFlow(QListWidget.LeftToRight)
            self.list_widget.setWrapping(True)
            self.list_widget.setResizeMode(QListWidget.Adjust)
            self.list_widget.setIconSize(QSize(120, 90))

            for project in self.projects:
                item = QListWidgetItem()
                item.setSizeHint(QSize(130, 170))
                self.list_widget.addItem(item)

                widget = ProjectGridItem(project)
                self.list_widget.setItemWidget(item, widget)

    def change_view_mode(self, mode):
        if self.current_view_mode != mode:
            self.current_view_mode = mode
            self.update_project_list()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ProjectListView()
    window.show()
    sys.exit(app.exec())