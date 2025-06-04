from PySide6.QtCore import Qt, QSize, QByteArray, QBuffer
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QFileDialog
import json
import os
import base64
from striprtf.striprtf import rtf_to_text


def split_text_by_line(text, max_length=6000):
    if not text:
        return []

    paragraphs = []
    current_paragraph = ""

    lines = text.split('\n')

    for line in lines:
        if len(current_paragraph) + len(line) + 1 > max_length:
            if current_paragraph:
                paragraphs.append(current_paragraph)
            current_paragraph = line
        else:
            if current_paragraph:
                current_paragraph += '\n' + line
            else:
                current_paragraph = line

    if current_paragraph:
        paragraphs.append(current_paragraph)

    return paragraphs


class Project:
    def __init__(self, name, author, modified_time, image, save_path):
        self.name = name
        self.author = author
        self.modified_time = modified_time
        self.image_size = QSize(60, 90)
        if type(image) is str:
            self.pixmap = QPixmap(image)
            self.pixmap = self.pixmap.scaled(QSize(60, 90),
                                             Qt.AspectRatioMode.KeepAspectRatio,
                                             Qt.TransformationMode.SmoothTransformation)
        else:
            self.pixmap = image
        self.save_path = save_path
        self.contents_path = os.path.join(self.save_path, self.name, "contents.json")
        self.highlight_path = os.path.join(self.save_path, self.name, "highlights.json")
        self.contents = []
        self.highlight_words_per_content = []
        self.total_pages = 0

    def load_contents(self, parent):
        if os.path.exists(self.contents_path):
            with open(self.contents_path, encoding='utf-8') as infile:
                self.contents = json.load(infile)
            with open(self.highlight_path, encoding='utf-8') as infile:
                self.highlight_words_per_content = json.load(infile)
        else:
            file_path, _ = QFileDialog.getOpenFileName(
                parent, "选择RTF文件", "", "RTF Files (*.rtf);;All Files (*)"
            )
            with open(file_path) as infile:
                content = infile.read()
                text = rtf_to_text(content)

            long_text = text.replace('‘', '\'').replace('’', '\'')
            self.contents = split_text_by_line(long_text, max_length=6000)

            self.highlight_words_per_content = [{} for _ in range(self.total_pages)]
            if not os.path.exists(os.path.dirname(self.contents_path)):
                os.makedirs(os.path.dirname(self.contents_path))
            with open(self.contents_path, 'w', encoding='utf-8') as f:
                json.dump(self.contents, f, ensure_ascii=False, indent=2)
            with open(self.highlight_path, 'w', encoding='utf-8') as f:
                json.dump(self.highlight_words_per_content, f, ensure_ascii=False, indent=2)
        self.total_pages = len(self.contents)

    def save_new_project_info(self):
        json_data = {}
        project_info_json_path = os.path.join(self.save_path, "project_info.json")
        if os.path.exists(project_info_json_path):
            with open(project_info_json_path, 'r', encoding='utf-8') as f:
                json_data = json.load(f)
        image = self.pixmap.toImage()
        byte_array = QByteArray()
        buffer = QBuffer(byte_array)
        buffer.open(QBuffer.OpenModeFlag.WriteOnly)
        image.save(buffer, "PNG")
        base64_data = base64.b64encode(byte_array).decode('utf-8')

        info = {
            "name": self.name,
            "author": self.author,
            "modified_time": self.modified_time,
            "image": base64_data
        }
        json_data.update({self.name: info})
        try:
            with open(project_info_json_path, 'w', encoding='utf-8') as f:
                json.dump(json_data, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"保存数据失败: {e}")

    def add_highlight_info(self, page, word, start, end):
        self.highlight_words_per_content[page][word] = [start, end]

    def save_highlight_info(self):
        with open(self.highlight_path, 'w', encoding='utf-8') as f:
            json.dump(self.highlight_words_per_content, f, ensure_ascii=False, indent=2)
