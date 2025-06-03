from ui import Ui_project_list
from PySide6.QtWidgets import (QFrame, QListWidget, QVBoxLayout, QHBoxLayout,
                               QWidget, QLabel, QListWidgetItem)
from PySide6.QtCore import QEvent, QSize, Signal, Qt


class ProjectListItem(QWidget):
    def __init__(self, project, parent=None):
        super().__init__(parent)
        self.setup_ui(project)

    def setup_ui(self, project):
        layout = QHBoxLayout(self)
        layout.setContentsMargins(5, 5, 5, 5)
        layout.setSpacing(10)

        cover_label = QLabel()
        cover_label.setFixedSize(project.image_size)
        cover_label.setPixmap(project.pixmap)

        layout.addWidget(cover_label)

        name_label = QLabel(project.name)
        font = name_label.font()
        font.setBold(True)
        name_label.setFont(font)
        name_label.setFixedWidth(200)
        name_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        layout.addWidget(name_label)

        author_label = QLabel(project.author)
        author_label.setFixedWidth(200)
        author_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        layout.addWidget(author_label)

        date_label = QLabel(project.modified_time)
        date_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        layout.addWidget(date_label, 1)


class ProjectWidgetListPage(QWidget, Ui_project_list):
    item_double_clicked_signal = Signal(QListWidgetItem)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.set_list_mode()
        self.project_widget_list.itemDoubleClicked.connect(self.on_item_double_clicked)

    def set_list_mode(self):
        self.project_widget_list.setViewMode(QListWidget.ListMode)
        self.project_widget_list.setFlow(QListWidget.TopToBottom)

        header_item = QListWidgetItem()
        header_item.setSizeHint(QSize(0, 30))
        self.project_widget_list.addItem(header_item)

        header_widget = QWidget()
        header_layout = QHBoxLayout(header_widget)
        header_layout.setContentsMargins(5, 5, 5, 5)
        header_layout.setSpacing(10)

        header_cover = QLabel("封面")
        header_cover.setFixedSize(60, 20)
        header_layout.addWidget(header_cover)

        header_name = QLabel("项目名称")
        header_name.setFixedWidth(200)
        font = header_name.font()
        font.setBold(True)
        header_name.setFont(font)
        header_layout.addWidget(header_name)

        header_author = QLabel("作者")
        header_author.setFixedWidth(200)
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

    def add_new_project(self, project):
        self.add_existent_project(project)
        project.save_new_project_info()

    def add_existent_project(self, project):
        item = QListWidgetItem()
        item.setSizeHint(QSize(0, 90))
        item.setData(Qt.UserRole, project.name)
        self.project_widget_list.addItem(item)

        widget = ProjectListItem(project)
        self.project_widget_list.setItemWidget(item, widget)

    def on_item_double_clicked(self, item):
        self.item_double_clicked_signal.emit(item)
