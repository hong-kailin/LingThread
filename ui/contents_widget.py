# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'contents_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTextEdit,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_contents_widget(object):
    def setupUi(self, contents_widget):
        if not contents_widget.objectName():
            contents_widget.setObjectName(u"contents_widget")
        contents_widget.resize(598, 667)
        contents_widget.setStyleSheet(u"#content {\n"
"    background-color: transparent;\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(contents_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.content = QTextEdit(contents_widget)
        self.content.setObjectName(u"content")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.content.sizePolicy().hasHeightForWidth())
        self.content.setSizePolicy(sizePolicy)
        self.content.setFrameShape(QFrame.Shape.NoFrame)

        self.verticalLayout.addWidget(self.content)

        self.widget = QWidget(contents_widget)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 40))
        self.widget.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.prev_btn = QPushButton(self.widget)
        self.prev_btn.setObjectName(u"prev_btn")

        self.horizontalLayout.addWidget(self.prev_btn)

        self.next_btn = QPushButton(self.widget)
        self.next_btn.setObjectName(u"next_btn")

        self.horizontalLayout.addWidget(self.next_btn)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(50, 0))
        self.label.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout.addWidget(self.label)

        self.page_line_edit = QLineEdit(self.widget)
        self.page_line_edit.setObjectName(u"page_line_edit")
        self.page_line_edit.setMinimumSize(QSize(40, 0))
        self.page_line_edit.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout.addWidget(self.page_line_edit)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)


        self.verticalLayout.addWidget(self.widget)


        self.retranslateUi(contents_widget)
        self.content.customContextMenuRequested.connect(contents_widget.show_text_menu)
        self.prev_btn.clicked.connect(contents_widget.prev_page)
        self.next_btn.clicked.connect(contents_widget.next_page)

        QMetaObject.connectSlotsByName(contents_widget)
    # setupUi

    def retranslateUi(self, contents_widget):
        contents_widget.setWindowTitle(QCoreApplication.translate("contents_widget", u"Form", None))
        self.prev_btn.setText(QCoreApplication.translate("contents_widget", u"\u4e0a\u4e00\u9875", None))
        self.next_btn.setText(QCoreApplication.translate("contents_widget", u"\u4e0b\u4e00\u9875", None))
        self.label.setText(QCoreApplication.translate("contents_widget", u"\u8df3\u8f6c\u5230\u7b2c", None))
        self.label_2.setText(QCoreApplication.translate("contents_widget", u"\u9875", None))
    # retranslateUi

