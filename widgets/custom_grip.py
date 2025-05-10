from PySide6.QtCore import Qt, QRect, QPoint
from PySide6.QtGui import QCursor
from PySide6.QtWidgets import QWidget, QSizeGrip, QHBoxLayout, QFrame


class CustomGrip(QWidget):
    def __init__(self, parent, position, disable_color=False):
        super().__init__(parent)
        self.parent = parent
        self.position = position
        self.disable_color = disable_color
        self.setup_ui()
        self.setup_behavior()

    def setup_ui(self):
        # 通用设置
        self.setAttribute(Qt.WA_StyledBackground)

        if self.position in (Qt.TopEdge, Qt.BottomEdge):
            self.setup_horizontal()
        else:
            self.setup_vertical()

    def setup_horizontal(self):
        self.setFixedHeight(10)
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        # 创建并保存中间拖拽条引用
        self.corner_left = self.create_corner(
            Qt.SizeFDiagCursor if self.position == Qt.TopEdge else Qt.SizeBDiagCursor
        )
        self.drag_bar = self.create_drag_bar(Qt.SizeVerCursor)  # 保存到实例变量
        self.corner_right = self.create_corner(
            Qt.SizeBDiagCursor if self.position == Qt.TopEdge else Qt.SizeFDiagCursor
        )

        layout.addWidget(self.corner_left)
        layout.addWidget(self.drag_bar)
        layout.addWidget(self.corner_right)

    def setup_vertical(self):
        self.setFixedWidth(10)
        self.drag_bar = QFrame(self)  # 显式创建drag_bar
        self.drag_bar.setCursor(QCursor(Qt.SizeHorCursor))
        self.drag_bar.setGeometry(QRect(0, 10, 10, self.parent.height() - 20))

        color = "#FF007F" if self.position == Qt.RightEdge else "#FF79C6"
        if self.disable_color:
            self.drag_bar.setStyleSheet("background: transparent")
        else:
            self.drag_bar.setStyleSheet(f"background: {color}")

    def create_corner(self, cursor_type):
        corner = QFrame()
        corner.setFixedSize(10, 10)
        corner.setCursor(QCursor(cursor_type))
        corner.setStyleSheet("background: transparent" if self.disable_color else "background: #21252B")
        return corner

    def create_drag_bar(self, cursor_type):
        bar = QFrame()
        bar.setCursor(QCursor(cursor_type))
        bar.setStyleSheet("background: transparent" if self.disable_color else "background: #00FFFF")
        return bar

    def setup_behavior(self):
        if self.position == Qt.TopEdge:
            self.setGeometry(0, 0, self.parent.width(), 10)
            self.drag_bar.mouseMoveEvent = self.resize_top
        elif self.position == Qt.BottomEdge:
            self.setGeometry(0, self.parent.height() - 10, self.parent.width(), 10)
            self.drag_bar.mouseMoveEvent = self.resize_bottom
        elif self.position == Qt.LeftEdge:
            self.setGeometry(0, 10, 10, self.parent.height() - 20)
            self.drag_bar.mouseMoveEvent = self.resize_left
        elif self.position == Qt.RightEdge:
            self.setGeometry(self.parent.width() - 10, 10, 10, self.parent.height() - 20)
            self.drag_bar.mouseMoveEvent = self.resize_right

    # 调整事件处理
    def resize_top(self, event):
        delta = event.position().toPoint()
        height = max(self.parent.minimumHeight(), self.parent.height() - delta.y())
        geo = self.parent.geometry()
        geo.setTop(geo.bottom() - height)
        self.parent.setGeometry(geo)

    def resize_bottom(self, event):
        delta = event.position().toPoint()
        self.parent.resize(self.parent.width(),
                           max(self.parent.minimumHeight(), self.parent.height() + delta.y()))

    def resize_left(self, event):
        delta = event.position().toPoint()
        width = max(self.parent.minimumWidth(), self.parent.width() - delta.x())
        geo = self.parent.geometry()
        geo.setLeft(geo.right() - width)
        self.parent.setGeometry(geo)

    def resize_right(self, event):
        delta = event.position().toPoint()
        self.parent.resize(max(self.parent.minimumWidth(), self.parent.width() + delta.x()),
                           self.parent.height())

    def resizeEvent(self, event):
        if self.position in (Qt.TopEdge, Qt.BottomEdge):
            self.setFixedWidth(self.parent.width())
        else:
            self.setFixedHeight(self.parent.height() - 20)
