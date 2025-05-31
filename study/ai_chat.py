import sys
import os
from openai import OpenAI
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                               QHBoxLayout, QTextEdit, QPushButton, QScrollArea,
                               QLabel, QSizePolicy, QFileDialog, QMessageBox, QLineEdit)
from PySide6.QtCore import Qt, QSize, QTimer, QThread, Signal
from PySide6.QtGui import QFont, QTextCursor, QColor, QPalette

client = OpenAI(api_key="sk-c8860ff4cb9246c28b3de26f0e00aff9", base_url="https://api.deepseek.com")


class MessageBubble(QWidget):
    """消息气泡组件"""

    def __init__(self, text, is_user=True, parent=None):
        super().__init__(parent)
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        self.is_user = is_user

        layout = QHBoxLayout(self)
        layout.setContentsMargins(10, 5, 10, 5)
        layout.setSpacing(10)

        # 创建消息标签
        message_label = QLabel(text)
        message_label.setWordWrap(True)
        message_label.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        message_label.setContentsMargins(10, 8, 10, 8)
        message_label.setStyleSheet("""
            QLabel {
                border-radius: 10px;
                padding: 8px 12px;
            }
        """)

        # 根据发送者设置不同样式
        if is_user:
            layout.addStretch()  # 用户消息靠右显示
            message_label.setStyleSheet(message_label.styleSheet() + """
                QLabel {
                    background-color: #DCF8C6;
                    color: #000000;
                }
            """)
        else:
            layout.addWidget(QLabel("AI:"))  # AI消息靠左显示，添加AI标识
            message_label.setStyleSheet(message_label.styleSheet() + """
                QLabel {
                    background-color: #F1F0F0;
                    color: #000000;
                }
            """)
        layout.addWidget(message_label)

        if not is_user:
            layout.addStretch()


class ApiCallThread(QThread):
    """API调用线程"""
    finished = Signal(str, bool)  # 信号，用于返回结果

    def __init__(self, client, messages):
        super().__init__()
        self.client = client
        self.messages = messages

    def run(self):
        try:
            # 调用API
            response = self.client.chat.completions.create(
                model="deepseek-chat",
                messages=self.messages,
                stream=False
            )

            # 获取回复内容
            ai_response = response.choices[0].message.content
            self.finished.emit(ai_response, True)
        except Exception as e:
            error_message = f"API调用错误: {str(e)}"
            self.finished.emit(error_message, False)


class ChatWindow(QMainWindow):
    """主聊天窗口"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("DeepSeek AI聊天助手")
        self.resize(600, 700)

        # 设置中文字体
        font = QFont()
        font.setFamily("SimHei")
        font.setPointSize(11)
        self.setFont(font)

        # 聊天历史
        self.chat_history = []

        # 创建主部件和布局
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)

        # 创建标题栏
        title_label = QLabel("DeepSeek AI聊天助手")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("""
            QLabel {
                background-color: #4A7ABC;
                color: white;
                font-size: 16px;
                font-weight: bold;
                padding: 10px;
            }
        """)
        main_layout.addWidget(title_label)

        # 创建聊天区域
        self.chat_area = QWidget()
        self.chat_area_layout = QVBoxLayout(self.chat_area)
        self.chat_area_layout.setAlignment(Qt.AlignTop)
        self.chat_area_layout.setContentsMargins(10, 10, 10, 10)
        self.chat_area_layout.setSpacing(10)

        # 创建滚动区域
        scroll_area = QScrollArea()
        scroll_area.setWidget(self.chat_area)
        scroll_area.setWidgetResizable(True)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        scroll_area.setStyleSheet("""
            QScrollArea {
                background-color: #FFFFFF;
                border: none;
            }
            QScrollBar:vertical {
                width: 8px;
                background: rgba(0,0,0,0);
                margin: 0px 0px 0px 0px;
            }
            QScrollBar::handle:vertical {
                background: rgba(0,0,0,20%);
                border-radius: 4px;
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                height: 0px;
            }
        """)
        main_layout.addWidget(scroll_area, 1)

        # 创建分隔线
        separator = QWidget()
        separator.setFixedHeight(1)
        separator.setStyleSheet("background-color: #CCCCCC;")
        main_layout.addWidget(separator)

        # 创建API密钥设置区域
        api_key_layout = QHBoxLayout()
        api_key_layout.setContentsMargins(10, 5, 10, 5)

        self.api_key_label = QLabel("API密钥:")
        self.api_key_input = QLineEdit()
        self.api_key_input.setEchoMode(QLineEdit.Password)
        self.api_key_input.setPlaceholderText("输入您的API密钥 (可选)")
        self.api_key_input.setToolTip("留空将使用环境变量中的API密钥")

        self.save_api_key_button = QPushButton("保存")
        self.save_api_key_button.setFixedWidth(60)
        self.save_api_key_button.clicked.connect(self.save_api_key)

        api_key_layout.addWidget(self.api_key_label)
        api_key_layout.addWidget(self.api_key_input)
        api_key_layout.addWidget(self.save_api_key_button)

        main_layout.addLayout(api_key_layout)

        # 创建输入区域
        input_layout = QHBoxLayout()
        input_layout.setContentsMargins(10, 5, 10, 10)
        input_layout.setSpacing(10)

        self.message_input = QTextEdit()
        self.message_input.setPlaceholderText("输入您的问题...")
        self.message_input.setMinimumHeight(50)
        self.message_input.setMaximumHeight(150)
        self.message_input.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.message_input.setStyleSheet("""
            QTextEdit {
                border: 1px solid #CCCCCC;
                border-radius: 5px;
                padding: 5px;
                font-size: 12px;
            }
        """)
        # 支持按Ctrl+Enter发送消息
        self.message_input.keyPressEvent = self.handle_key_press
        input_layout.addWidget(self.message_input)

        self.send_button = QPushButton("发送")
        self.send_button.setFixedSize(80, 50)
        self.send_button.setStyleSheet("""
            QPushButton {
                background-color: #4A7ABC;
                color: white;
                border-radius: 5px;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #3A6AB8;
            }
            QPushButton:pressed {
                background-color: #2A5AA8;
            }
        """)
        self.send_button.clicked.connect(self.send_message)
        input_layout.addWidget(self.send_button)

        main_layout.addLayout(input_layout)

        # 添加欢迎消息
        self.add_message("您好！我是基于DeepSeek模型的AI助手，有什么可以帮助您的吗？", False)

        # 存储正在思考的消息widget
        self.thinking_message = None

    def handle_key_press(self, event):
        """处理键盘事件，支持Ctrl+Enter发送消息"""
        if event.key() == Qt.Key_Return and event.modifiers() & Qt.ControlModifier:
            self.send_message()
        else:
            # 调用原始的keyPressEvent处理其他情况
            QTextEdit.keyPressEvent(self.message_input, event)

    def save_api_key(self):
        pass
        # """保存API密钥"""
        # api_key = self.api_key_input.text().strip()
        # if api_key:
        #     openai.api_key = api_key
        #     QMessageBox.information(self, "成功", "API密钥已保存")
        # else:
        #     QMessageBox.warning(self, "警告", "API密钥不能为空")

    def add_message(self, text, is_user=True):
        """添加消息到聊天区域"""
        message_bubble = MessageBubble(text, is_user)
        self.chat_area_layout.addWidget(message_bubble)

        # 滚动到底部
        QApplication.processEvents()
        scroll_bar = self.findChild(QScrollArea).verticalScrollBar()
        scroll_bar.setValue(scroll_bar.maximum())

        # 如果是"正在思考"消息，保存引用
        if not is_user and "正在思考" in text:
            self.thinking_message = message_bubble

        # 如果是用户消息，添加到聊天历史
        if is_user:
            self.chat_history.append({"role": "user", "content": text})

        return message_bubble

    def remove_thinking_message(self):
        """移除"正在思考"消息"""
        if self.thinking_message and self.chat_area_layout.indexOf(self.thinking_message) != -1:
            self.chat_area_layout.removeWidget(self.thinking_message)
            self.thinking_message.setParent(None)
            self.thinking_message = None

    def send_message(self):
        """发送消息"""
        text = self.message_input.toPlainText().strip()
        if text:
            # 添加用户消息
            self.add_message(text, True)

            # 清空输入框
            self.message_input.clear()

            # 添加"正在思考"消息
            self.add_message("正在思考您的问题...", False)

            # 启动API调用线程
            self.api_thread = ApiCallThread(client, [
                {"role": "system", "content": "You are a helpful assistant"}] + self.chat_history)
            self.api_thread.finished.connect(self.on_api_response)
            self.api_thread.start()

    def on_api_response(self, response_text, success):
        """处理API响应"""
        # 移除"正在思考"消息
        self.remove_thinking_message()

        if success:
            # 添加AI回复
            self.add_message(response_text, False)
            # 添加到聊天历史
            self.chat_history.append({"role": "assistant", "content": response_text})
        else:
            # 显示错误消息
            self.add_message(response_text, False)


if __name__ == "__main__":
    # 确保中文显示正常
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)

    app = QApplication(sys.argv)

    # 设置全局样式
    app.setStyle("Fusion")
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(245, 245, 245))
    palette.setColor(QPalette.WindowText, Qt.black)
    palette.setColor(QPalette.Base, QColor(255, 255, 255))
    palette.setColor(QPalette.AlternateBase, QColor(240, 240, 240))
    palette.setColor(QPalette.ToolTipBase, Qt.white)
    palette.setColor(QPalette.ToolTipText, Qt.black)
    palette.setColor(QPalette.Text, Qt.black)
    palette.setColor(QPalette.Button, QColor(240, 240, 240))
    palette.setColor(QPalette.ButtonText, Qt.black)
    palette.setColor(QPalette.BrightText, Qt.red)
    palette.setColor(QPalette.Link, QColor(42, 130, 218))
    palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    palette.setColor(QPalette.HighlightedText, Qt.white)
    app.setPalette(palette)

    window = ChatWindow()
    window.show()

    sys.exit(app.exec())