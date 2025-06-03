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
    def __init__(self, name, author, modified_time, image, path):
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

        self.contents = []
        self.highlight_words_per_content = []
        self.load_contents(path)

    def load_contents(self, path):
        json_path = os.path.join(path, self.name, "contents.json")
        if os.path.exists(json_path):
            with open(json_path) as infile:
                self.contents = json.load(infile)
        else:
            file_path, _ = QFileDialog.getOpenFileName(
                self, "选择RTF文件", "", "RTF Files (*.rtf);;All Files (*)"
            )
            with open(file_path) as infile:
                content = infile.read()
                text = rtf_to_text(content)

            long_text = text.replace('‘', '\'').replace('’', '\'')
            self.contents = split_text_by_line(long_text, max_length=6000)
            self.total_pages = len(self.contents)

            with open(json_path, 'w', encoding='utf-8') as f:
                json.dump(self.contents, f, ensure_ascii=False, indent=2)
