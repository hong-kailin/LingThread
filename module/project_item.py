from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QPalette


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

        cover_label = QLabel()
        cover_label.setFixedSize(80, 60)
        cover_label.setAutoFillBackground(True)
        palette = cover_label.palette()
        palette.setColor(QPalette.Window, QColor(project.color))
        cover_label.setPalette(palette)
        layout.addWidget(cover_label)

        name_label = QLabel(project.name)
        font = name_label.font()
        font.setBold(True)
        name_label.setFont(font)
        name_label.setFixedWidth(150)
        name_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        layout.addWidget(name_label)

        author_label = QLabel(project.author)
        author_label.setFixedWidth(100)
        author_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        layout.addWidget(author_label)

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

        cover_label = QLabel()
        cover_label.setFixedSize(120, 90)
        cover_label.setAutoFillBackground(True)
        palette = cover_label.palette()
        palette.setColor(QPalette.Window, QColor(project.color))
        cover_label.setPalette(palette)
        layout.addWidget(cover_label, alignment=Qt.AlignCenter)

        name_label = QLabel(project.name)
        name_label.setAlignment(Qt.AlignCenter)
        font = name_label.font()
        font.setBold(True)
        name_label.setFont(font)
        name_label.setWordWrap(True)
        layout.addWidget(name_label)

        author_label = QLabel(f"作者: {project.author}")
        author_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(author_label)

        date_label = QLabel(f"{project.modified_date}")
        date_label.setAlignment(Qt.AlignCenter)
        date_label.setStyleSheet("color: #666666; font-size: 10pt;")
        layout.addWidget(date_label)
