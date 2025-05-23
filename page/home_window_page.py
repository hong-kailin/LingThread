from PySide6.QtCore import QObject, QPropertyAnimation, Property, QEasingCurve
from PySide6.QtWidgets import QWidget
from ui import Ui_home_widget


class SplitterAnimationHelper(QObject):
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
        current_sizes = []
        for i in range(len(self.start_sizes)):
            size = self.start_sizes[i] + (self.target_sizes[i] - self.start_sizes[i]) * progress
            current_sizes.append(size)

        self.splitter.setSizes(current_sizes)

    progress = Property(float, getProgress, setProgress)


class HomeWindowPage(QWidget, Ui_home_widget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        initial_sizes = [100, 0, 0, 0]
        self.visible_states = [True, False, False, False]
        self.splitter.setSizes(initial_sizes)
        self.last_sizes = [100, 200, 200, 200]

        self.time_amimation = 500

        self.animation_helper = SplitterAnimationHelper(self.splitter)
        self.animation = QPropertyAnimation(self.animation_helper, b"progress")
        self.animation.setDuration(500)
        self.animation.setEasingCurve(QEasingCurve.InOutCubic)

    def show_hide_card(self, widget_index):
        if self.animation.state() == QPropertyAnimation.Running:
            return

        current_sizes = self.splitter.sizes()

        if self.visible_states[widget_index]:
            self.last_sizes[widget_index] = current_sizes[widget_index]
            target_width = current_sizes[widget_index]

            target_sizes = current_sizes.copy()
            target_sizes[0] += target_width
            target_sizes[widget_index] = 0
        else:
            restore_width = self.last_sizes[widget_index]

            target_sizes = current_sizes.copy()
            target_sizes[0] -= restore_width  # 第0个widget减少宽度
            target_sizes[widget_index] = restore_width  # 恢复目标widget宽度

        self.animation_helper.setStartSizes(current_sizes)
        self.animation_helper.setTargetSizes(target_sizes)
        self.animation.setStartValue(0.0)
        self.animation.setEndValue(1.0)

        self.animation.start()
        self.visible_states[widget_index] = not self.visible_states[widget_index]

    def show_hide_word_card(self):
        self.show_hide_card(3)

    def show_hide_sentence_card(self):
        self.show_hide_card(2)

    def show_hide_ai_chat_card(self):
        self.show_hide_card(1)
