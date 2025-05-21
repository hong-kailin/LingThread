# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_window.ui'
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
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_new_window(object):
    def setupUi(self, new_window):
        if not new_window.objectName():
            new_window.setObjectName(u"new_window")
        new_window.resize(530, 360)
        new_window.setMinimumSize(QSize(530, 360))
        new_window.setMaximumSize(QSize(530, 360))
        new_window.setStyleSheet(u"#cover_label{\n"
"	border: 5px dashed rgb(37,47,82);\n"
"}\n"
"\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"\n"
"#new_window{\n"
"	background-color:rgb(63, 114, 175);\n"
"}\n"
"\n"
"QLineEdit {\n"
"        border: none;\n"
"        border-bottom: 1px solid #CCCCCC;\n"
"        background-color: transparent;\n"
"        padding: 2px;\n"
"        selection-background-color: #a8c7fe;\n"
"}\n"
"QLineEdit:focus {\n"
"        border-bottom: 2px solid rgb(37,47,82);\n"
"        outline: none;\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color:rgb(37,47,82);\n"
"    background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(new_window)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(9, 0, -1, 0)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.cover_label = QLabel(new_window)
        self.cover_label.setObjectName(u"cover_label")
        self.cover_label.setMinimumSize(QSize(200, 300))
        self.cover_label.setMaximumSize(QSize(200, 300))
        self.cover_label.setStyleSheet(u"")
        self.cover_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_5.addWidget(self.cover_label, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.frame = QFrame(new_window)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 40))
        self.lineEdit.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.verticalLayout.addWidget(self.lineEdit)

        self.lineEdit_2 = QLineEdit(self.frame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(0, 40))
        self.lineEdit_2.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.verticalLayout.addWidget(self.lineEdit_2)

        self.lineEdit_3 = QLineEdit(self.frame)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMinimumSize(QSize(0, 40))
        self.lineEdit_3.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)
        self.lineEdit_3.setReadOnly(True)

        self.verticalLayout.addWidget(self.lineEdit_3)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(103, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.cancel_btn = QPushButton(self.frame_2)
        self.cancel_btn.setObjectName(u"cancel_btn")

        self.horizontalLayout.addWidget(self.cancel_btn)

        self.comfirm_btn = QPushButton(self.frame_2)
        self.comfirm_btn.setObjectName(u"comfirm_btn")

        self.horizontalLayout.addWidget(self.comfirm_btn)


        self.verticalLayout_3.addWidget(self.frame_2, 0, Qt.AlignmentFlag.AlignBottom)


        self.horizontalLayout_5.addWidget(self.frame)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)


        self.retranslateUi(new_window)

        QMetaObject.connectSlotsByName(new_window)
    # setupUi

    def retranslateUi(self, new_window):
        new_window.setWindowTitle(QCoreApplication.translate("new_window", u"Form", None))
        self.cover_label.setText(QCoreApplication.translate("new_window", u"Click to select the cover image", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("new_window", u"Name:", None))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("new_window", u"Author:", None))
        self.lineEdit_3.setText("")
        self.cancel_btn.setText(QCoreApplication.translate("new_window", u"Cancel", None))
        self.comfirm_btn.setText(QCoreApplication.translate("new_window", u"Comfirm", None))
    # retranslateUi

