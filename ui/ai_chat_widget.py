# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ai_chat_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPlainTextEdit,
    QPushButton, QScrollArea, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_ai_chat_widget(object):
    def setupUi(self, ai_chat_widget):
        if not ai_chat_widget.objectName():
            ai_chat_widget.setObjectName(u"ai_chat_widget")
        ai_chat_widget.resize(256, 540)
        self.verticalLayout = QVBoxLayout(ai_chat_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(ai_chat_widget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.scrollArea = QScrollArea(ai_chat_widget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 236, 410))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.plainTextEdit = QPlainTextEdit(ai_chat_widget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setMinimumSize(QSize(0, 80))
        self.plainTextEdit.setMaximumSize(QSize(16777215, 80))

        self.horizontalLayout.addWidget(self.plainTextEdit, 0, Qt.AlignmentFlag.AlignBottom)

        self.pushButton = QPushButton(ai_chat_widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 80))
        self.pushButton.setMaximumSize(QSize(16777215, 80))

        self.horizontalLayout.addWidget(self.pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(ai_chat_widget)

        QMetaObject.connectSlotsByName(ai_chat_widget)
    # setupUi

    def retranslateUi(self, ai_chat_widget):
        ai_chat_widget.setWindowTitle(QCoreApplication.translate("ai_chat_widget", u"Form", None))
        self.label.setText(QCoreApplication.translate("ai_chat_widget", u"LingThread AI\u804a\u5929\u52a9\u624b", None))
        self.pushButton.setText(QCoreApplication.translate("ai_chat_widget", u"send", None))
    # retranslateUi

