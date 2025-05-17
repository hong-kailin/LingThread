# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'register.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
                            QSize)
from PySide6.QtWidgets import (QFormLayout, QLabel, QLineEdit,
                               QPushButton, QWidget)


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(500, 450)
        Form.setMinimumSize(QSize(500, 450))
        Form.setMaximumSize(QSize(500, 450))
        Form.setStyleSheet(u"QWidget#Form{\n"
"	border-image: url(:/images/images/images/LingThread_ori.png);\n"
"}")
        self.main_menu_btn = QPushButton(Form)
        self.main_menu_btn.setObjectName(u"main_menu_btn")
        self.main_menu_btn.setGeometry(QRect(30, 20, 41, 41))
        self.main_menu_btn.setStyleSheet(u"QPushButton{\n"
"	border-radius:20px;\n"
"	background-color:rgb(255, 170, 255);\n"
"    border: 2px solid rgb(250,10, 2);\n"
"    color:rgb(255, 255, 255)\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border:4px double rgb(0, 255, 255)\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	background-color:rgb(50, 17, 255);\n"
"}")
        self.main_menu_btn.setCheckable(True)
        self.main_menu_btn.setChecked(False)
        self.about_menu_btn = QPushButton(Form)
        self.about_menu_btn.setObjectName(u"about_menu_btn")
        self.about_menu_btn.setGeometry(QRect(100, 20, 41, 41))
        self.about_menu_btn.setStyleSheet(u"QPushButton{\n"
"	border-radius:20px;\n"
"	background-color:rgb(255, 170, 255);\n"
"    border: 2px solid rgb(250,10, 2);\n"
"    color:rgb(255, 255, 255)\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border:4px double rgb(0, 255, 255)\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color:rgb(50, 17, 255);\n"
"}")
        self.reset_menu_btn = QPushButton(Form)
        self.reset_menu_btn.setObjectName(u"reset_menu_btn")
        self.reset_menu_btn.setGeometry(QRect(90, 80, 41, 41))
        self.reset_menu_btn.setStyleSheet(u"QPushButton{\n"
"	border-radius:20px;\n"
"	background-color:rgb(255, 170, 255);\n"
"    border: 2px solid rgb(250,10, 2);\n"
"    color:rgb(255, 255, 255)\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border:4px double rgb(0, 255, 255)\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color:rgb(50, 17, 255);\n"
"}")
        self.exit_menu_btn = QPushButton(Form)
        self.exit_menu_btn.setObjectName(u"exit_menu_btn")
        self.exit_menu_btn.setGeometry(QRect(30, 90, 41, 41))
        self.exit_menu_btn.setStyleSheet(u"QPushButton{\n"
"	border-radius:20px;\n"
"	background-color:rgb(255, 170, 255);\n"
"    border: 2px solid rgb(250,10, 2);\n"
"    color:rgb(255, 255, 255)\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border:4px double rgb(0, 255, 255)\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color:rgb(50, 17, 255);\n"
"}")
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(170, 180, 281, 233))
        self.formLayout = QFormLayout(self.layoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setVerticalSpacing(20)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 14pt \"Bauhaus 93\";\n"
"color: rgb(255, 255, 0);")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label)

        self.account_le = QLineEdit(self.layoutWidget)
        self.account_le.setObjectName(u"account_le")
        self.account_le.setMinimumSize(QSize(0, 40))
        self.account_le.setStyleSheet(u"background-color:transparent;\n"
"color: rgb(85, 0, 255);")
        self.account_le.setClearButtonEnabled(True)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.account_le)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font: 14pt \"Bauhaus 93\";\n"
"color: rgb(255, 255, 0);")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.password_le = QLineEdit(self.layoutWidget)
        self.password_le.setObjectName(u"password_le")
        self.password_le.setMinimumSize(QSize(0, 40))
        self.password_le.setStyleSheet(u"background-color:transparent;\n"
"color: rgb(85, 0, 255);")
        self.password_le.setClearButtonEnabled(True)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.password_le)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font: 14pt \"Bauhaus 93\";\n"
"color: rgb(255, 255, 0);")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.confirm_pwd_le = QLineEdit(self.layoutWidget)
        self.confirm_pwd_le.setObjectName(u"confirm_pwd_le")
        self.confirm_pwd_le.setMinimumSize(QSize(0, 40))
        self.confirm_pwd_le.setStyleSheet(u"background-color:transparent;\n"
"color: rgb(85, 0, 255);")
        self.confirm_pwd_le.setClearButtonEnabled(True)

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.confirm_pwd_le)

        self.register_btn = QPushButton(self.layoutWidget)
        self.register_btn.setObjectName(u"register_btn")
        self.register_btn.setEnabled(False)
        self.register_btn.setMinimumSize(QSize(0, 45))
        self.register_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 85, 0);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(55, 85, 0);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(120, 85, 30);\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"	background-color: rgb(10, 85, 30);\n"
"}")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.SpanningRole, self.register_btn)


        self.retranslateUi(Form)
        self.about_menu_btn.clicked.connect(Form.about_lk)
        self.reset_menu_btn.clicked.connect(Form.reset)
        self.exit_menu_btn.clicked.connect(Form.exit)
        self.register_btn.clicked.connect(Form.check_register)
        self.main_menu_btn.clicked["bool"].connect(Form.show_hide_menu)
        self.account_le.textChanged.connect(Form.enable_register_btn)
        self.password_le.textChanged.connect(Form.enable_register_btn)
        self.confirm_pwd_le.textChanged.connect(Form.enable_register_btn)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.main_menu_btn.setText(QCoreApplication.translate("Form", u"\u83dc\u5355", None))
        self.about_menu_btn.setText(QCoreApplication.translate("Form", u"\u5173\u4e8e", None))
        self.reset_menu_btn.setText(QCoreApplication.translate("Form", u"\u91cd\u7f6e", None))
        self.exit_menu_btn.setText(QCoreApplication.translate("Form", u"\u9000\u51fa", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u8d26   \u53f7\uff1a", None))
        self.account_le.setText("")
        self.label_2.setText(QCoreApplication.translate("Form", u"\u5bc6   \u7801\uff1a", None))
        self.password_le.setText("")
        self.label_3.setText(QCoreApplication.translate("Form", u"\u786e\u8ba4\u5bc6\u7801\uff1a", None))
        self.confirm_pwd_le.setText("")
        self.register_btn.setText(QCoreApplication.translate("Form", u"\u6ce8\u518c", None))
    # retranslateUi

