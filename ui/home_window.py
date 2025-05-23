# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'home_window.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QSizePolicy, QSplitter,
    QWidget)

class Ui_home_widget(object):
    def setupUi(self, home_widget):
        if not home_widget.objectName():
            home_widget.setObjectName(u"home_widget")
        home_widget.resize(780, 635)
        home_widget.setStyleSheet(u"#edit_widget{\n"
"	background-color:rgb(37, 47, 82);\n"
"}\n"
"\n"
"#ai_chat_widget{\n"
"	background-color:#dbe2ef;\n"
"}\n"
"#word_card_widget{\n"
"	background-color:rgb(17,45,78);\n"
"}\n"
"#sentence_card_widget{\n"
"	background-color:rgb(63,114,175);\n"
"}")
        self.horizontalLayout = QHBoxLayout(home_widget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.splitter = QSplitter(home_widget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.splitter.setHandleWidth(0)
        self.edit_widget = QWidget(self.splitter)
        self.edit_widget.setObjectName(u"edit_widget")
        self.splitter.addWidget(self.edit_widget)
        self.ai_chat_widget = QWidget(self.splitter)
        self.ai_chat_widget.setObjectName(u"ai_chat_widget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ai_chat_widget.sizePolicy().hasHeightForWidth())
        self.ai_chat_widget.setSizePolicy(sizePolicy)
        self.ai_chat_widget.setMaximumSize(QSize(16777215, 16777215))
        self.splitter.addWidget(self.ai_chat_widget)
        self.word_card_widget = QWidget(self.splitter)
        self.word_card_widget.setObjectName(u"word_card_widget")
        sizePolicy.setHeightForWidth(self.word_card_widget.sizePolicy().hasHeightForWidth())
        self.word_card_widget.setSizePolicy(sizePolicy)
        self.word_card_widget.setMaximumSize(QSize(16777215, 16777215))
        self.splitter.addWidget(self.word_card_widget)
        self.sentence_card_widget = QWidget(self.splitter)
        self.sentence_card_widget.setObjectName(u"sentence_card_widget")
        sizePolicy.setHeightForWidth(self.sentence_card_widget.sizePolicy().hasHeightForWidth())
        self.sentence_card_widget.setSizePolicy(sizePolicy)
        self.sentence_card_widget.setMinimumSize(QSize(0, 0))
        self.sentence_card_widget.setMaximumSize(QSize(16777215, 16777215))
        self.splitter.addWidget(self.sentence_card_widget)

        self.horizontalLayout.addWidget(self.splitter)


        self.retranslateUi(home_widget)

        QMetaObject.connectSlotsByName(home_widget)
    # setupUi

    def retranslateUi(self, home_widget):
        home_widget.setWindowTitle(QCoreApplication.translate("home_widget", u"Form", None))
    # retranslateUi

