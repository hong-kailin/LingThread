from PySide6.QtCore import Qt
from PySide6.QtGui import QCursor
from PySide6.QtWidgets import QWidget, QSizeGrip


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
