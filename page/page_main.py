from ui import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Qt, QEvent, QTimer, QPropertyAnimation, QEasingCurve, QParallelAnimationGroup
from PySide6.QtGui import QIcon
from widgets import CustomGrip


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.titleRightInfo.installEventFilter(self)
        self.closeAppBtn.clicked.connect(lambda: self.close())

        self.top_grip = CustomGrip(self, Qt.TopEdge, True)
        self.bottom_grip = CustomGrip(self, Qt.BottomEdge, True)
        self.left_grip = CustomGrip(self, Qt.LeftEdge, True)
        self.right_grip = CustomGrip(self, Qt.RightEdge, True)

        def open_close_left_box():
            self.toggle_left_box(True)

        self.toggleLeftBox.clicked.connect(open_close_left_box)
        self.extraCloseColumnBtn.clicked.connect(open_close_left_box)

    def toggle_left_box(self, enable):
        if enable:
            # GET WIDTH
            width = self.extraLeftBox.width()
            widthRightBox = self.extraRightBox.width()
            maxExtend = 240
            color = "background-color: rgb(44, 49, 58);"
            standard = 0

            # GET BTN STYLE
            style = self.toggleLeftBox.styleSheet()

            # SET MAX WIDTH
            if width == 0:
                widthExtended = maxExtend
                # SELECT BTN
                self.toggleLeftBox.setStyleSheet(style + color)
                if widthRightBox != 0:
                    style = self.settingsTopBtn.styleSheet()
                    self.settingsTopBtn.setStyleSheet(style.replace("background-color: #ff79c6;", ''))
            else:
                widthExtended = standard
                # RESET BTN
                self.toggleLeftBox.setStyleSheet(style.replace(color, ''))

        self.start_box_animation(width, widthRightBox, "left")

    def start_box_animation(self, left_box_width, right_box_width, direction):
        right_width = 0
        left_width = 0

        # Check values
        if left_box_width == 0 and direction == "left":
            left_width = 240
        else:
            left_width = 0
        # Check values
        if right_box_width == 0 and direction == "right":
            right_width = 240
        else:
            right_width = 0

            # ANIMATION LEFT BOX
        self.left_box = QPropertyAnimation(self.extraLeftBox, b"minimumWidth")
        self.left_box.setDuration(500)
        self.left_box.setStartValue(left_box_width)
        self.left_box.setEndValue(left_width)
        self.left_box.setEasingCurve(QEasingCurve.InOutQuart)

        # ANIMATION RIGHT BOX
        self.right_box = QPropertyAnimation(self.extraRightBox, b"minimumWidth")
        self.right_box.setDuration(500)
        self.right_box.setStartValue(right_box_width)
        self.right_box.setEndValue(right_width)
        self.right_box.setEasingCurve(QEasingCurve.InOutQuart)

        # GROUP ANIMATION
        self.group = QParallelAnimationGroup()
        self.group.addAnimation(self.left_box)
        self.group.addAnimation(self.right_box)
        self.group.start()

    def eventFilter(self, obj, event):
        if obj == self.titleRightInfo and event.type() == QEvent.MouseButtonDblClick:
            QTimer.singleShot(250, self.maximize_restore)
            return True
        return super().eventFilter(obj, event)

    def maximize_restore(self):
        main_window = self.window()
        if not main_window.isMaximized():
            main_window.showMaximized()
            self.maximizeRestoreAppBtn.setToolTip("Restore")
            self.maximizeRestoreAppBtn.setIcon(QIcon(u":/icons/images/icons/icon_restore.png"))
            self.frame_size_grip.hide()
            self.left_grip.hide()
            self.right_grip.hide()
            self.top_grip.hide()
            self.bottom_grip.hide()
        else:
            main_window = self.window()
            main_window.showNormal()
            self.resize(self.width() + 1, self.height() + 1)
            self.maximizeRestoreAppBtn.setToolTip("Maximize")
            self.maximizeRestoreAppBtn.setIcon(QIcon(u":/icons/images/icons/icon_maximize.png"))
            self.frame_size_grip.show()
            self.left_grip.show()
            self.right_grip.show()
            self.top_grip.show()
            self.bottom_grip.show()

    def resizeEvent(self, event):
        # Update Size Grips
        self.left_grip.setGeometry(0, 10, 10, self.height() - 20)
        self.right_grip.setGeometry(self.width() - 10, 10, 10, self.height() - 20)
        self.top_grip.setGeometry(0, 0, self.width(), 10)
        self.bottom_grip.setGeometry(0, self.height() - 10, self.width(), 10)
