import sys
import json
import base64
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QVBoxLayout,
                               QLabel, QFileDialog, QWidget, QMessageBox)
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtCore import QByteArray, QBuffer, Qt


class ImageSerializer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("图片序列化工具")
        self.setGeometry(100, 100, 600, 500)

        # 创建中心部件和布局
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # 创建图片显示标签
        self.image_label = QLabel("请选择一张图片")
        self.image_label.setStyleSheet("border: 1px solid #ccc;")
        self.image_label.setMinimumSize(400, 300)
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.image_label)

        # 创建按钮
        self.load_button = QPushButton("加载图片")
        self.load_button.clicked.connect(self.load_image)
        layout.addWidget(self.load_button)

        self.save_button = QPushButton("保存到JSON")
        self.save_button.clicked.connect(self.save_to_json)
        self.save_button.setEnabled(False)
        layout.addWidget(self.save_button)

        self.load_json_button = QPushButton("从JSON加载")
        self.load_json_button.clicked.connect(self.load_from_json)
        layout.addWidget(self.load_json_button)

        # 存储图片数据
        self.image_data = None
        self.current_image_path = None

    def load_image(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "选择图片", "", "图片文件 (*.png *.jpg *.jpeg *.bmp)"
        )
        if file_path:
            self.current_image_path = file_path
            pixmap = QPixmap(file_path)
            self.image_label.setPixmap(pixmap.scaled(
                self.image_label.size(),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            ))
            self.save_button.setEnabled(True)

            # 读取图片数据并转换为字节数组
            image = QImage(file_path)
            byte_array = QByteArray()
            buffer = QBuffer(byte_array)
            buffer.open(QBuffer.OpenModeFlag.WriteOnly)
            image.save(buffer, "PNG")
            self.image_data = byte_array

    def save_to_json(self):
        if self.image_data is None:
            QMessageBox.warning(self, "警告", "没有加载图片")
            return

        # 选择保存路径
        file_path, _ = QFileDialog.getSaveFileName(
            self, "保存JSON文件", "", "JSON文件 (*.json)"
        )
        if not file_path:
            return

        try:
            # 将图片数据转换为Base64编码
            base64_data = base64.b64encode(self.image_data).decode('utf-8')

            # 创建JSON数据
            json_data = {
                "image_format": "PNG",
                "image_data": base64_data,
                "original_path": self.current_image_path
            }

            # 保存到JSON文件
            with open(file_path, 'w') as f:
                json.dump(json_data, f, indent=4)

            QMessageBox.information(self, "成功", f"图片已保存到 {file_path}")
        except Exception as e:
            QMessageBox.critical(self, "错误", f"保存失败: {str(e)}")

    def load_from_json(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "选择JSON文件", "", "JSON文件 (*.json)"
        )
        if file_path:
            try:
                # 从JSON文件读取数据
                with open(file_path, 'r') as f:
                    json_data = json.load(f)

                # 获取Base64编码的图片数据
                base64_data = json_data.get("image_data", "")
                if not base64_data:
                    QMessageBox.warning(self, "警告", "JSON文件中没有图片数据")
                    return

                # 解码Base64数据
                image_data = base64.b64decode(base64_data)

                # 创建QPixmap并显示
                pixmap = QPixmap()
                pixmap.loadFromData(image_data)
                self.image_label.setPixmap(pixmap.scaled(
                    self.image_label.size(),
                    Qt.AspectRatioMode.KeepAspectRatio,
                    Qt.TransformationMode.SmoothTransformation
                ))

                self.image_data = QByteArray(image_data)
                self.save_button.setEnabled(True)

                # 显示原始路径信息
                original_path = json_data.get("original_path", "未知")
                self.setWindowTitle(f"图片序列化工具 - 原始路径: {original_path}")

            except Exception as e:
                QMessageBox.critical(self, "错误", f"加载失败: {str(e)}")


if __name__ == "__main__":
    # 确保中文显示正常
    QApplication.setApplicationName("图片序列化工具")

    app = QApplication(sys.argv)
    window = ImageSerializer()
    window.show()
    sys.exit(app.exec())
