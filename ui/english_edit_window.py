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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QPushButton,
    QSizePolicy, QTextEdit, QVBoxLayout, QWidget)
import resources_rc

class Ui_english_edit_widget(object):
    def setupUi(self, english_edit_widget):
        if not english_edit_widget.objectName():
            english_edit_widget.setObjectName(u"english_edit_widget")
        english_edit_widget.resize(226, 667)
        english_edit_widget.setStyleSheet(u"#english_edit {\n"
"    background-color: transparent;\n"
"}\n"
"#info_edit {\n"
"    background-color: transparent;\n"
"}\n"
"QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"QPushButton:hover { background-color: rgb(44, 49, 57); border-style: solid; border-radius: 4px; }\n"
"QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }")
        self.verticalLayout = QVBoxLayout(english_edit_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.english_edit = QTextEdit(english_edit_widget)
        self.english_edit.setObjectName(u"english_edit")
        self.english_edit.setFrameShape(QFrame.Shape.NoFrame)

        self.verticalLayout.addWidget(self.english_edit)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.info_edit = QTextEdit(english_edit_widget)
        self.info_edit.setObjectName(u"info_edit")
        self.info_edit.setMinimumSize(QSize(0, 100))
        self.info_edit.setMaximumSize(QSize(16777215, 100))
        self.info_edit.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.info_edit, 0, Qt.AlignmentFlag.AlignBottom)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.edit_btn = QPushButton(english_edit_widget)
        self.edit_btn.setObjectName(u"edit_btn")
        self.edit_btn.setMinimumSize(QSize(28, 28))
        self.edit_btn.setMaximumSize(QSize(28, 28))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/cil-pencil.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.edit_btn.setIcon(icon)

        self.verticalLayout_2.addWidget(self.edit_btn)

        self.read_btn = QPushButton(english_edit_widget)
        self.read_btn.setObjectName(u"read_btn")
        self.read_btn.setMinimumSize(QSize(28, 28))
        self.read_btn.setMaximumSize(QSize(28, 28))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/cil-volume-high.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.read_btn.setIcon(icon1)

        self.verticalLayout_2.addWidget(self.read_btn)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(english_edit_widget)

        QMetaObject.connectSlotsByName(english_edit_widget)
    # setupUi

    def retranslateUi(self, english_edit_widget):
        english_edit_widget.setWindowTitle(QCoreApplication.translate("english_edit_widget", u"Form", None))
        self.edit_btn.setText("")
        self.read_btn.setText("")
    # retranslateUi

