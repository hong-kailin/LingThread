# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'container_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QScrollArea,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_container_widget(object):
    def setupUi(self, container_widget):
        if not container_widget.objectName():
            container_widget.setObjectName(u"container_widget")
        container_widget.resize(211, 741)
        container_widget.setStyleSheet(u"QScrollArea {\n"
"    background-color: transparent;\n"
"}\n"
"#contents, #transparent_space{\n"
"    background-color: transparent;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(container_widget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(container_widget)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.scrollArea.setWidgetResizable(True)
        self.contents = QWidget()
        self.contents.setObjectName(u"contents")
        self.contents.setGeometry(QRect(0, 0, 211, 741))
        self.container_layout = QVBoxLayout(self.contents)
        self.container_layout.setSpacing(0)
        self.container_layout.setObjectName(u"container_layout")
        self.container_layout.setContentsMargins(0, 0, 0, 0)
        self.transparent_space = QWidget(self.contents)
        self.transparent_space.setObjectName(u"transparent_space")
        self.transparent_space.setMinimumSize(QSize(0, 500))

        self.container_layout.addWidget(self.transparent_space)

        self.scrollArea.setWidget(self.contents)

        self.verticalLayout_2.addWidget(self.scrollArea)


        self.retranslateUi(container_widget)

        QMetaObject.connectSlotsByName(container_widget)
    # setupUi

    def retranslateUi(self, container_widget):
        container_widget.setWindowTitle(QCoreApplication.translate("container_widget", u"Form", None))
    # retranslateUi

