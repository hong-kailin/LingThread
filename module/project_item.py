from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel
from PySide6.QtCore import Qt, QSize, QByteArray, QBuffer
from PySide6.QtGui import QColor, QPalette, QPixmap
import json
import base64


class Project:
    def __init__(self, name, author, modified_time, image_path):
        self.name = name
        self.author = author
        self.modified_time = modified_time
        self.image_size = QSize(60, 90)
        self.pixmap = QPixmap(image_path)
        self.pixmap = self.pixmap.scaled(QSize(60, 90),
                                       Qt.AspectRatioMode.KeepAspectRatio,
                                       Qt.TransformationMode.SmoothTransformation)

    def save(self, path):
        image = self.pixmap.toImage()
        byte_array = QByteArray()
        buffer = QBuffer(byte_array)
        buffer.open(QBuffer.OpenModeFlag.WriteOnly)
        image.save(buffer, "PNG")
        base64_data = base64.b64encode(byte_array).decode('utf-8')

        data = {
            "name": self.name,
            "author": self.author,
            "modified_time": self.modified_time,
            "image": base64_data
        }

        try:
            with open(path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"保存数据失败: {e}")


class ProjectListItem(QWidget):
    def __init__(self, project, parent=None):
        super().__init__(parent)
        self.setup_ui(project)
        project.save("./data/project_items.json")

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


class ProjectGridItem(QWidget):
    def __init__(self, project, parent=None):
        super().__init__(parent)
        self.setup_ui(project)

    def setup_ui(self, project):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(5, 5, 5, 5)
        layout.setSpacing(5)

        cover_label = QLabel()
        cover_label.setFixedSize(60, 90)
        # cover_label.setAutoFillBackground(True)
        # palette = cover_label.palette()
        # palette.setColor(QPalette.Window, QColor(project.color))
        # cover_label.setPalette(palette)
        cover_label.setPixmap(project.image)
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
