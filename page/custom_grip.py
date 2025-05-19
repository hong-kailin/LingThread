# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

from PySide6.QtCore import Qt
from PySide6.QtGui import QCursor
from PySide6.QtWidgets import QWidget


class CustomGrip(QWidget):
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
