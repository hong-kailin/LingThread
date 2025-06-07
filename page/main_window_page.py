from ui import Ui_main_window
from PySide6.QtCore import Qt, QPropertyAnimation, QEasingCurve, Signal, QEvent, QTimer
from PySide6.QtGui import QIcon, QCursor
from PySide6.QtWidgets import QWidget, QSizeGrip, QVBoxLayout


class CustomCornerGrip(QSizeGrip):
    def __init__(self, parent=None, position=None):
        super().__init__(parent)
        if position != "RightBottom":
            self.setStyleSheet("""
                QSizeGrip {
                    background-color: transparent;  
                    width: 16px;                  
                    height: 16px;
                }
            """)
        if position == "LeftTop":
            self.setGeometry(0, 0, 10, 10)
            self.setCursor(QCursor(Qt.SizeFDiagCursor))
        elif position == "LeftBottom":
            self.setGeometry(0, parent.height() - 10, 10, 10)
            self.setCursor(QCursor(Qt.SizeBDiagCursor))
        elif position == "RightTop":
            self.setGeometry(parent.width() - 10, 0, 10, 10)
            self.setCursor(QCursor(Qt.SizeFDiagCursor))
        elif position == "RightBottom":
            self.setGeometry(parent.width() - 10, parent.height() - 10, 10, 10)
            self.setCursor(QCursor(Qt.SizeBDiagCursor))
        # self.setStyleSheet("background-color: green;")


class CustomEdgeGrip(QWidget):
    def __init__(self, parent=None, position=None):
        super().__init__(parent)
        self.position = position
        if position == Qt.TopEdge:
            self.setGeometry(10, 0, parent.width() - 20, 10)
            self.setCursor(QCursor(Qt.SizeVerCursor))
        elif position == Qt.BottomEdge:
            self.setGeometry(10, parent.height() - 10, parent.width() - 20, 10)
            self.setCursor(QCursor(Qt.SizeVerCursor))
        elif position == Qt.LeftEdge:
            self.setGeometry(0, 10, 10, parent.height() - 20)
            self.setCursor(QCursor(Qt.SizeHorCursor))
        elif position == Qt.RightEdge:
            self.setGeometry(parent.width() - 10, 10, 10, parent.height() - 20)
            self.setCursor(QCursor(Qt.SizeHorCursor))
        # self.setStyleSheet("background-color: red;")
        # self.setAttribute(Qt.WA_StyledBackground, True)

    def mouseMoveEvent(self, event):
        delta = event.pos()
        geo = self.parent().geometry()

        if self.position == Qt.TopEdge:
            height = max(self.parent().minimumHeight(), self.parent().height() - delta.y())
            geo.setTop(geo.bottom() - height)
        elif self.position == Qt.BottomEdge:
            height = max(self.parent().minimumHeight(), self.parent().height() + delta.y())
            geo.setBottom(geo.top() + height)
        elif self.position == Qt.LeftEdge:
            width = max(self.parent().minimumWidth(), self.parent().width() - delta.x())
            geo.setLeft(geo.right() - width)
        elif self.position == Qt.RightEdge:
            width = max(self.parent().minimumWidth(), self.parent().width() + delta.x())
            geo.setRight(geo.left() + width)
        self.parent().setGeometry(geo)


class MainWindowPage(QWidget, Ui_main_window):
    create_new_project_signal = Signal()
    show_hide_ai_chat_card_signal = Signal()
    show_hide_word_card_signal = Signal()
    show_hide_sentence_card_signal = Signal()
    show_project_list_signal = Signal()
    save_current_project_info_signal = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowFlags(Qt.FramelessWindowHint)
        # self.setAttribute(Qt.WA_TranslucentBackground)
        self.setupUi(self)

        self.left_grip = CustomEdgeGrip(self, Qt.LeftEdge)
        self.right_grip = CustomEdgeGrip(self, Qt.RightEdge)
        self.top_grip = CustomEdgeGrip(self, Qt.TopEdge)
        self.bottom_grip = CustomEdgeGrip(self, Qt.BottomEdge)

        self.left_top_grip = CustomCornerGrip(self, "LeftTop")
        self.left_bottom_grip = CustomCornerGrip(self, "LeftBottom")
        self.right_top_grip = CustomCornerGrip(self, "RightTop")
        self.right_bottom_grip = CustomCornerGrip(self, "RightBottom")

        self.set_top_line_behavior()

        # setting
        self.time_amimation = 500

    def set_top_line_behavior(self):
        def press_window(event):
            self.grag_pos = event.globalPos()

        def move_window(event):
            # IF MAXIMIZED CHANGE TO NORMAL
            if self.isMaximized():
                self.maximize_restore()
            # MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.grag_pos)
                self.grag_pos = event.globalPos()

        def double_click_maximize_restore(event):
            if event.type() == QEvent.MouseButtonDblClick:
                QTimer.singleShot(250, lambda: self.maximize_restore())

        self.top_line.mousePressEvent = press_window
        self.top_line.mouseMoveEvent = move_window
        self.top_line.mouseDoubleClickEvent = double_click_maximize_restore

    def show_hide_btn_name(self, flag):
        if flag:
            width = 60
            widthExtended = 170
        else:
            width = 170
            widthExtended = 60
        self.animation = QPropertyAnimation(self.left_sider_bar, b"minimumWidth")
        self.animation.setDuration(self.time_amimation)
        self.animation.setStartValue(width)
        self.animation.setEndValue(widthExtended)
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()

    def resizeEvent(self, event):
        self.top_grip.setGeometry(10, 0, self.width() - 20, 10)
        self.bottom_grip.setGeometry(10, self.height() - 10, self.width() - 20, 10)
        self.left_grip.setGeometry(0, 10, 10, self.height() - 20)
        self.right_grip.setGeometry(self.width() - 10, 10, 10, self.height() - 20)

        self.left_top_grip.setGeometry(0, 0, 10, 10)
        self.left_bottom_grip.setGeometry(0, self.height() - 10, 10, 10)
        self.right_top_grip.setGeometry(self.width() - 10, 0, 10, 10)
        self.right_bottom_grip.setGeometry(self.width() - 10, self.height() - 10, 10, 10)

    def maximize_restore(self):
        if not self.isMaximized():
            self.maximize_restore_btn.setToolTip("Restore")
            self.maximize_restore_btn.setIcon(QIcon(u":/icons/images/icons/icon_restore.png"))
            self.showMaximized()
        else:
            self.maximize_restore_btn.setToolTip("Maximize")
            self.maximize_restore_btn.setIcon(QIcon(u":/icons/images/icons/icon_maximize.png"))
            self.showNormal()

    def show_hide_left_box(self):
        self.animation = QPropertyAnimation(self.left_hide_box, b"minimumWidth")
        self.animation.setDuration(self.time_amimation)
        if self.left_hide_box.width() == 0:
            self.animation.setStartValue(0)
            self.animation.setEndValue(240)

        else:
            self.animation.setStartValue(240)
            self.animation.setEndValue(0)
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()

    def create_new_project(self):
        self.create_new_project_signal.emit()

    def show_hide_word_card(self):
        self.show_hide_word_card_signal.emit()

    def show_hide_sentence_card(self):
        self.show_hide_sentence_card_signal.emit()

    def show_hide_ai_chat_card(self):
        self.show_hide_ai_chat_card_signal.emit()

    def page_number_update(self, number):
        info = "current page is " + str(number)
        self.page_info.setText(info)

    def show_project_list(self):
        self.show_project_list_signal.emit()

    def save_current_project_info(self):
        self.save_current_project_info_signal.emit()
