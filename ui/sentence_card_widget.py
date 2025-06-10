# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sentence_card_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_sentence_card_widget(object):
    def setupUi(self, sentence_card_widget):
        if not sentence_card_widget.objectName():
            sentence_card_widget.setObjectName(u"sentence_card_widget")
        sentence_card_widget.resize(281, 98)
        sentence_card_widget.setStyleSheet(u"#sentence{\n"
"	background-color:rgb(63,114,175);\n"
"	border-radius: 5px;\n"
"     margin: 5px;\n"
"     border: 1px solid #dee2e6;\n"
"}\n"
"#translate{\n"
"	background-color:rgb(17, 45, 78); \n"
"	border-radius: 5px;\n"
"     margin: 5px;\n"
"     border: 1px solid #dee2e6;\n"
"}")
        self.verticalLayout = QVBoxLayout(sentence_card_widget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.sentence = QLabel(sentence_card_widget)
        self.sentence.setObjectName(u"sentence")
        self.sentence.setMinimumSize(QSize(0, 30))
        self.sentence.setWordWrap(True)

        self.verticalLayout.addWidget(self.sentence)

        self.translate = QTextEdit(sentence_card_widget)
        self.translate.setObjectName(u"translate")
        self.translate.setMinimumSize(QSize(0, 30))

        self.verticalLayout.addWidget(self.translate)


        self.retranslateUi(sentence_card_widget)
        self.translate.textChanged.connect(sentence_card_widget.translate_height_change)

        QMetaObject.connectSlotsByName(sentence_card_widget)
    # setupUi

    def retranslateUi(self, sentence_card_widget):
        sentence_card_widget.setWindowTitle(QCoreApplication.translate("sentence_card_widget", u"Form", None))
        self.sentence.setText(QCoreApplication.translate("sentence_card_widget", u"TextLabel", None))
    # retranslateUi

