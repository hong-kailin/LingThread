from ui import Ui_project_list
from module import ProjectListItem, ProjectGridItem, Project
from PySide6.QtWidgets import (QFrame, QListWidget, QVBoxLayout, QHBoxLayout,
                               QWidget, QLabel, QListWidgetItem)
from PySide6.QtCore import QEvent, QSize


class ProjectWidgetListPage(QWidget, Ui_project_list):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.projects = self.create_sample_projects()
        self.create_sample_projects()
        self.set_list_mode()

    def create_sample_projects(self):
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

    def set_list_mode(self):
        self.project_widget_list.setViewMode(QListWidget.ListMode)
        self.project_widget_list.setFlow(QListWidget.TopToBottom)
        self.project_widget_list.setIconSize(QSize(80, 60))

        header_item = QListWidgetItem()
        header_item.setSizeHint(QSize(0, 30))
        self.project_widget_list.addItem(header_item)

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

        header_widget.setStyleSheet("background-color: #000010;")
        self.project_widget_list.setItemWidget(header_item, header_widget)

        line_item = QListWidgetItem()
        line_item.setSizeHint(QSize(0, 2))
        self.project_widget_list.addItem(line_item)
        line_widget = QFrame()
        line_widget.setFrameShape(QFrame.HLine)
        line_widget.setFrameShadow(QFrame.Sunken)
        self.project_widget_list.setItemWidget(line_item, line_widget)

        for project in self.projects:
            item = QListWidgetItem()
            item.setSizeHint(QSize(0, 70))
            self.project_widget_list.addItem(item)

            widget = ProjectListItem(project)
            self.project_widget_list.setItemWidget(item, widget)
