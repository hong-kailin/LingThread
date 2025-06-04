# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'word_card_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QSizePolicy,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_word_card_widget(object):
    def setupUi(self, word_card_widget):
        if not word_card_widget.objectName():
            word_card_widget.setObjectName(u"word_card_widget")
        word_card_widget.resize(279, 321)
        word_card_widget.setStyleSheet(u"#label{\n"
"	background-color:rgb(17, 45, 78);\n"
"	border-radius: 5px;\n"
"     margin: 5px;\n"
"     border: 1px solid #dee2e6;\n"
"}\n"
"#mean_edit, \n"
"#mean_remember_edit, \n"
"#other_edit, \n"
"#pronunciation_remember_edit, \n"
"#pronunciation_edit{\n"
"	background-color:rgb(63,114,175);\n"
"	border-radius: 5px;\n"
"     margin: 5px;\n"
"     border: 1px solid #dee2e6;\n"
"}")
        self.verticalLayout = QVBoxLayout(word_card_widget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(word_card_widget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(0, 30))
        self.label.setMaximumSize(QSize(16777215, 30))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.widget = QWidget(word_card_widget)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.mean_edit = QTextEdit(self.widget)
        self.mean_edit.setObjectName(u"mean_edit")
        self.mean_edit.setMinimumSize(QSize(0, 30))

        self.verticalLayout_2.addWidget(self.mean_edit, 0, Qt.AlignmentFlag.AlignTop)

        self.pronunciation_edit = QTextEdit(self.widget)
        self.pronunciation_edit.setObjectName(u"pronunciation_edit")
        self.pronunciation_edit.setMinimumSize(QSize(0, 30))

        self.verticalLayout_2.addWidget(self.pronunciation_edit, 0, Qt.AlignmentFlag.AlignTop)

        self.mean_remember_edit = QTextEdit(self.widget)
        self.mean_remember_edit.setObjectName(u"mean_remember_edit")
        self.mean_remember_edit.setMinimumSize(QSize(0, 30))

        self.verticalLayout_2.addWidget(self.mean_remember_edit, 0, Qt.AlignmentFlag.AlignTop)

        self.pronunciation_remember_edit = QTextEdit(self.widget)
        self.pronunciation_remember_edit.setObjectName(u"pronunciation_remember_edit")
        self.pronunciation_remember_edit.setMinimumSize(QSize(0, 30))

        self.verticalLayout_2.addWidget(self.pronunciation_remember_edit, 0, Qt.AlignmentFlag.AlignTop)

        self.other_edit = QTextEdit(self.widget)
        self.other_edit.setObjectName(u"other_edit")
        self.other_edit.setMinimumSize(QSize(0, 30))

        self.verticalLayout_2.addWidget(self.other_edit, 0, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout.addWidget(self.widget)


        self.retranslateUi(word_card_widget)
        self.mean_edit.textChanged.connect(word_card_widget.mean_height_change)
        self.pronunciation_edit.textChanged.connect(word_card_widget.pronunciation_height_change)
        self.mean_remember_edit.textChanged.connect(word_card_widget.mean_remember_height_change)
        self.pronunciation_remember_edit.textChanged.connect(word_card_widget.pronunciation_remember_height_change)
        self.other_edit.textChanged.connect(word_card_widget.other_height_change)

        QMetaObject.connectSlotsByName(word_card_widget)
    # setupUi

    def retranslateUi(self, word_card_widget):
        word_card_widget.setWindowTitle(QCoreApplication.translate("word_card_widget", u"Frame", None))
        self.label.setText(QCoreApplication.translate("word_card_widget", u"TextLabel", None))
        self.mean_edit.setPlaceholderText(QCoreApplication.translate("word_card_widget", u"\u8bf7\u8f93\u5165\u542b\u4e49", None))
        self.pronunciation_edit.setPlaceholderText(QCoreApplication.translate("word_card_widget", u"\u8bf7\u8f93\u5165\u8bfb\u97f3", None))
        self.mean_remember_edit.setPlaceholderText(QCoreApplication.translate("word_card_widget", u"\u8bf7\u8f93\u5165\u542b\u4e49\u52a9\u8bb0", None))
        self.pronunciation_remember_edit.setPlaceholderText(QCoreApplication.translate("word_card_widget", u"\u8bf7\u8f93\u5165\u53d1\u97f3\u52a9\u8bb0", None))
        self.other_edit.setPlaceholderText(QCoreApplication.translate("word_card_widget", u"\u5176\u4ed6", None))
    # retranslateUi

