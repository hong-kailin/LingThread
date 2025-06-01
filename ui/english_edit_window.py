# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'english_edit_window.ui'
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

class Ui_english_edit_widget(object):
    def setupUi(self, english_edit_widget):
        if not english_edit_widget.objectName():
            english_edit_widget.setObjectName(u"english_edit_widget")
        english_edit_widget.resize(598, 667)
        english_edit_widget.setStyleSheet(u"#english_edit {\n"
"    background-color: transparent;\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(english_edit_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.english_edit = QTextEdit(english_edit_widget)
        self.english_edit.setObjectName(u"english_edit")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.english_edit.sizePolicy().hasHeightForWidth())
        self.english_edit.setSizePolicy(sizePolicy)
        self.english_edit.setFrameShape(QFrame.Shape.NoFrame)

        self.verticalLayout.addWidget(self.english_edit)

        self.widget = QWidget(english_edit_widget)
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

        self.load_rtf_btn = QPushButton(self.widget)
        self.load_rtf_btn.setObjectName(u"load_rtf_btn")

        self.horizontalLayout.addWidget(self.load_rtf_btn)


        self.verticalLayout.addWidget(self.widget)


        self.retranslateUi(english_edit_widget)
        self.english_edit.customContextMenuRequested.connect(english_edit_widget.show_text_menu)
        self.load_rtf_btn.clicked.connect(english_edit_widget.load_rtf_file)

        QMetaObject.connectSlotsByName(english_edit_widget)
    # setupUi

    def retranslateUi(self, english_edit_widget):
        english_edit_widget.setWindowTitle(QCoreApplication.translate("english_edit_widget", u"Form", None))
        self.prev_btn.setText(QCoreApplication.translate("english_edit_widget", u"\u4e0a\u4e00\u9875", None))
        self.next_btn.setText(QCoreApplication.translate("english_edit_widget", u"\u4e0b\u4e00\u9875", None))
        self.label.setText(QCoreApplication.translate("english_edit_widget", u"\u8df3\u8f6c\u5230\u7b2c", None))
        self.label_2.setText(QCoreApplication.translate("english_edit_widget", u"\u9875", None))
        self.load_rtf_btn.setText(QCoreApplication.translate("english_edit_widget", u"\u5bfc\u5165RTF\u6587\u4ef6", None))
    # retranslateUi

