# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_new_dialog(object):
    def setupUi(self, new_dialog):
        if not new_dialog.objectName():
            new_dialog.setObjectName(u"new_dialog")
        new_dialog.resize(530, 360)
        new_dialog.setMinimumSize(QSize(530, 360))
        new_dialog.setMaximumSize(QSize(530, 360))
        new_dialog.setStyleSheet(u"#cover_label{\n"
"	border: 5px dashed rgb(37,47,82);\n"
"}\n"
"\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"\n"
"#new_dialog{\n"
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
        new_dialog.setModal(True)
        self.verticalLayout_2 = QVBoxLayout(new_dialog)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(9, 0, 9, 0)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.cover_label = QLabel(new_dialog)
        self.cover_label.setObjectName(u"cover_label")
        self.cover_label.setMinimumSize(QSize(200, 300))
        self.cover_label.setMaximumSize(QSize(200, 300))
        self.cover_label.setStyleSheet(u"")
        self.cover_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_5.addWidget(self.cover_label, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.frame = QFrame(new_dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.name_edit = QLineEdit(self.frame)
        self.name_edit.setObjectName(u"name_edit")
        self.name_edit.setMinimumSize(QSize(0, 40))
        self.name_edit.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.verticalLayout.addWidget(self.name_edit)

        self.author_edit = QLineEdit(self.frame)
        self.author_edit.setObjectName(u"author_edit")
        self.author_edit.setMinimumSize(QSize(0, 40))
        self.author_edit.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.verticalLayout.addWidget(self.author_edit)

        self.time_label = QLabel(self.frame)
        self.time_label.setObjectName(u"time_label")
        self.time_label.setMinimumSize(QSize(0, 60))
        self.time_label.setMaximumSize(QSize(16777215, 60))

        self.verticalLayout.addWidget(self.time_label)


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


        self.retranslateUi(new_dialog)
        self.cancel_btn.clicked.connect(new_dialog.close)
        self.comfirm_btn.clicked.connect(new_dialog.create_new_project)

        QMetaObject.connectSlotsByName(new_dialog)
    # setupUi

    def retranslateUi(self, new_dialog):
        new_dialog.setWindowTitle(QCoreApplication.translate("new_dialog", u"Dialog", None))
        self.cover_label.setText(QCoreApplication.translate("new_dialog", u"Click to select the cover image", None))
        self.name_edit.setText("")
        self.name_edit.setPlaceholderText(QCoreApplication.translate("new_dialog", u"Name:", None))
        self.author_edit.setText("")
        self.author_edit.setPlaceholderText(QCoreApplication.translate("new_dialog", u"Author:", None))
        self.time_label.setText("")
        self.cancel_btn.setText(QCoreApplication.translate("new_dialog", u"Cancel", None))
        self.comfirm_btn.setText(QCoreApplication.translate("new_dialog", u"Comfirm", None))
    # retranslateUi

