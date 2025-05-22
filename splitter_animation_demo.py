import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QPushButton,
                               QHBoxLayout, QVBoxLayout, QSplitter)
from PySide6.QtCore import QPropertyAnimation, QEasingCurve, Qt, QObject, Property


class SplitterAnimationHelper(QObject):
    """辅助类，用于处理分割器动画"""

    def __init__(self, splitter, parent=None):
        super().__init__(parent)
        self.splitter = splitter
        self.start_sizes = []
        self.target_sizes = []

    def setStartSizes(self, sizes):
        self.start_sizes = sizes

    def setTargetSizes(self, sizes):
        self.target_sizes = sizes

    def getProgress(self):
        return 0.0

    def setProgress(self, progress):
        # 根据进度计算当前大小
        current_sizes = []
        for i in range(len(self.start_sizes)):
            size = self.start_sizes[i] + (self.target_sizes[i] - self.start_sizes[i]) * progress
            current_sizes.append(size)

        # 更新分割器大小
        self.splitter.setSizes(current_sizes)

    # 创建一个可动画的进度属性
    progress = Property(float, getProgress, setProgress)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Multi Widget Splitter Animation")
        self.setGeometry(100, 100, 1000, 600)

        # 创建主部件和布局
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        # 创建水平分割器
        self.splitter = QSplitter(Qt.Horizontal)

        # 创建4个widget并添加到分割器
        self.widgets = []
        self.visible_states = []
        self.last_sizes = []  # 保存每个widget的最后大小

        colors = ["#e0e0e0", "#d0d0d0", "#c0c0c0", "#b0b0b0"]
        total_width = 1000  # 初始总宽度
        initial_width = total_width // 4  # 平均宽度

        for i in range(4):
            widget = QWidget()
            widget.setStyleSheet(f"background-color: {colors[i]};")
            self.splitter.addWidget(widget)

            # 记录可见状态和最后大小
            if i == 0:  # 第一个widget默认可见
                self.visible_states.append(True)
                self.last_sizes.append(initial_width)
            else:  # 后三个widget默认隐藏
                self.visible_states.append(False)
                self.last_sizes.append(initial_width)

        # 设置初始大小 - 第一个widget占据全部宽度，其他为0
        initial_sizes = [total_width, 0, 0, 0]
        self.splitter.setSizes(initial_sizes)

        # 创建3个控制按钮
        button_layout = QHBoxLayout()
        self.buttons = []

        for i in range(3):
            button = QPushButton(f"显示面板 {i + 2}")
            button.clicked.connect(lambda checked, idx=i: self.toggle_widget(idx + 1))
            button_layout.addWidget(button)
            self.buttons.append(button)

        # 添加到主布局
        main_layout.addWidget(self.splitter)
        main_layout.addLayout(button_layout)

        # 创建动画辅助对象
        self.animation_helper = SplitterAnimationHelper(self.splitter)

        # 动画对象
        self.animation = QPropertyAnimation(self.animation_helper, b"progress")
        self.animation.setDuration(500)
        self.animation.setEasingCurve(QEasingCurve.InOutCubic)

    def toggle_widget(self, widget_index):
        """切换指定索引widget的显示/隐藏状态"""
        if self.animation.state() == QPropertyAnimation.Running:
            return  # 正在动画中，忽略新请求

        current_sizes = self.splitter.sizes()

        if self.visible_states[widget_index]:
            # 隐藏widget前保存当前大小
            self.last_sizes[widget_index] = current_sizes[widget_index]

            # 计算目标大小 - 只调整第0个widget的大小
            target_width = current_sizes[widget_index]  # 要隐藏的widget宽度

            target_sizes = current_sizes.copy()
            target_sizes[0] += target_width  # 第0个widget增加宽度
            target_sizes[widget_index] = 0  # 目标widget宽度为0

            self.buttons[widget_index - 1].setText(f"显示面板 {widget_index + 1}")
        else:
            # 恢复widget - 只调整第0个widget的大小
            restore_width = self.last_sizes[widget_index]

            target_sizes = current_sizes.copy()
            target_sizes[0] -= restore_width  # 第0个widget减少宽度
            target_sizes[widget_index] = restore_width  # 恢复目标widget宽度

            self.buttons[widget_index - 1].setText(f"隐藏面板 {widget_index + 1}")

        # 设置动画
        self.animation_helper.setStartSizes(current_sizes)
        self.animation_helper.setTargetSizes(target_sizes)
        self.animation.setStartValue(0.0)
        self.animation.setEndValue(1.0)

        # 开始动画
        self.animation.start()
        self.visible_states[widget_index] = not self.visible_states[widget_index]


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())