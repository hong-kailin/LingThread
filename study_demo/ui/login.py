# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Login_Form(object):
    def setupUi(self, Login_Form):
        if not Login_Form.objectName():
            Login_Form.setObjectName(u"Login_Form")
        Login_Form.resize(517, 500)
        self.verticalLayout = QVBoxLayout(Login_Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(Login_Form)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background-color: rgb(85, 255, 127);")
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(Login_Form)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"background-color: rgb(170, 170, 255);")
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.widget_2)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignBottom)

        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setStyleSheet(u"background-color: rgb(0, 170, 255);")
        self.gridLayout = QGridLayout(self.widget_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.checkBox_2 = QCheckBox(self.widget_3)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.gridLayout.addWidget(self.checkBox_2, 2, 1, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.comboBox = QComboBox(self.widget_3)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(0, 50))

        self.gridLayout.addWidget(self.comboBox, 0, 0, 1, 2)

        self.pushButton_3 = QPushButton(self.widget_3)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(0, 60))

        self.gridLayout.addWidget(self.pushButton_3, 3, 0, 1, 2)

        self.checkBox = QCheckBox(self.widget_3)
        self.checkBox.setObjectName(u"checkBox")

        self.gridLayout.addWidget(self.checkBox, 2, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.lineEdit = QLineEdit(self.widget_3)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 50))

        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 2)


        self.horizontalLayout.addWidget(self.widget_3)

        self.pushButton_2 = QPushButton(self.widget_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QSize(80, 80))
        self.pushButton_2.setMaximumSize(QSize(80, 80))

        self.horizontalLayout.addWidget(self.pushButton_2, 0, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignBottom)

        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 5)
        self.horizontalLayout.setStretch(2, 2)

        self.verticalLayout.addWidget(self.widget_2)

        self.verticalLayout.setStretch(0, 3)
        self.verticalLayout.setStretch(1, 5)

        self.retranslateUi(Login_Form)
        self.pushButton.clicked.connect(Login_Form.show_register_pane)

        QMetaObject.connectSlotsByName(Login_Form)
    # setupUi

    def retranslateUi(self, Login_Form):
        Login_Form.setWindowTitle(QCoreApplication.translate("Login_Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Login_Form", u"TextLabel", None))
        self.pushButton.setText(QCoreApplication.translate("Login_Form", u"\u6ce8\u518c\u8d26\u53f7", None))
        self.checkBox_2.setText(QCoreApplication.translate("Login_Form", u"\u8bb0\u4f4f\u5bc6\u7801", None))
        self.pushButton_3.setText(QCoreApplication.translate("Login_Form", u"\u5b89\u5168\u767b\u5f55", None))
        self.checkBox.setText(QCoreApplication.translate("Login_Form", u"\u81ea\u52a8\u767b\u5f55", None))
        self.pushButton_2.setText(QCoreApplication.translate("Login_Form", u"\u4e8c\u7ef4\u7801", None))
    # retranslateUi

