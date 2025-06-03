# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'left_box.ui'
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
    QPushButton, QSizePolicy, QTextEdit, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_left_box(object):
    def setupUi(self, left_box):
        if not left_box.objectName():
            left_box.setObjectName(u"left_box")
        left_box.resize(240, 607)
        left_box.setMaximumSize(QSize(240, 16777215))
        left_box.setStyleSheet(u"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"\n"
"#setting_icon {\n"
"	background-image: url(:/icons/images/icons/icon_settings.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#widget{\n"
"	background-color:rgb(189, 147, 249);\n"
"}\n"
"#left_box{\n"
"	background-color:rgb(63, 114, 175);\n"
"}\n"
"\n"
"\n"
"\n"
"/* Extra Top Menus */\n"
"#widget_2 .QPushButton {\n"
"background-color:rgb(63, 114, 175);\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#widget_2 .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#widget_2 .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"#widget .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#widget .QPushButton:hover { "
                        "background-color: rgb(44, 49, 57); border-style: solid; border-radius: 4px; }\n"
"#widget .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"\n"
"QTextEdit {\n"
"	background-color: rgb(63, 114, 175);\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"")
        self.verticalLayout = QVBoxLayout(left_box)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(left_box)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 50))
        self.widget.setMaximumSize(QSize(16777215, 50))
        self.widget.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 0, 10, 0)
        self.setting_icon = QLabel(self.widget)
        self.setting_icon.setObjectName(u"setting_icon")
        self.setting_icon.setMinimumSize(QSize(20, 20))
        self.setting_icon.setMaximumSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.setting_icon)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(20, 20))
        self.pushButton.setMaximumSize(QSize(20, 20))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon)

        self.horizontalLayout.addWidget(self.pushButton)


        self.verticalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(left_box)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_2 = QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.tutorial_link = QPushButton(self.widget_2)
        self.tutorial_link.setObjectName(u"tutorial_link")
        self.tutorial_link.setMinimumSize(QSize(0, 45))
        self.tutorial_link.setMaximumSize(QSize(16777215, 45))
        self.tutorial_link.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-house.png);")

        self.verticalLayout_2.addWidget(self.tutorial_link)

        self.code_link = QPushButton(self.widget_2)
        self.code_link.setObjectName(u"code_link")
        self.code_link.setMinimumSize(QSize(0, 45))
        self.code_link.setMaximumSize(QSize(16777215, 45))
        self.code_link.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-lightbulb.png);")

        self.verticalLayout_2.addWidget(self.code_link)

        self.wechat_qrcode = QPushButton(self.widget_2)
        self.wechat_qrcode.setObjectName(u"wechat_qrcode")
        self.wechat_qrcode.setMinimumSize(QSize(0, 45))
        self.wechat_qrcode.setMaximumSize(QSize(16777215, 45))
        self.wechat_qrcode.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-chat-bubble.png);")

        self.verticalLayout_2.addWidget(self.wechat_qrcode)

        self.text_edit = QTextEdit(self.widget_2)
        self.text_edit.setObjectName(u"text_edit")
        self.text_edit.setFrameShape(QFrame.Shape.NoFrame)
        self.text_edit.setFrameShadow(QFrame.Shadow.Sunken)
        self.text_edit.setLineWidth(1)
        self.text_edit.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)
        self.text_edit.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)

        self.verticalLayout_2.addWidget(self.text_edit)


        self.verticalLayout.addWidget(self.widget_2)


        self.retranslateUi(left_box)
        self.pushButton.clicked.connect(left_box.close_left_box)

        QMetaObject.connectSlotsByName(left_box)
    # setupUi

    def retranslateUi(self, left_box):
        left_box.setWindowTitle(QCoreApplication.translate("left_box", u"Form", None))
        self.setting_icon.setText("")
        self.label_2.setText(QCoreApplication.translate("left_box", u"  Left Box", None))
        self.pushButton.setText("")
        self.tutorial_link.setText(QCoreApplication.translate("left_box", u"Tutorial Link", None))
        self.code_link.setText(QCoreApplication.translate("left_box", u"Code Link", None))
        self.wechat_qrcode.setText(QCoreApplication.translate("left_box", u"Wechat Qrcode", None))
        self.text_edit.setMarkdown(QCoreApplication.translate("left_box", u"**LingThread**\n"
"\n"
"An interface created using Python and PySide (support for PyQt), and with\n"
"colors based on the Dracula theme created by Zeno Rocha.\n"
"\n"
"MIT License\n"
"\n"
"Created by: \u6bd4\u98de\u9e1f\u8d35\u91cd\u7684\u591a_HKL\n"
"\n"
"**Convert UI**\n"
"\n"
"pyside6-uic main.ui > ui_main.py\n"
"\n"
"**Convert QRC**\n"
"\n"
"pyside6-rcc resources.qrc -o resources_rc.py\n"
"\n"
"", None))
        self.text_edit.setHtml(QCoreApplication.translate("left_box", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">LingThread</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">An interface created using Python and PySide (support for PyQt), and with colors based on the Dracula theme created by Ze"
                        "no Rocha.</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">MIT License</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#bd93f9;\">Created by: \u6bd4\u98de\u9e1f\u8d35\u91cd\u7684\u591a_HKL</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">Convert UI</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">pyside6-uic main.ui &gt; ui_main.py</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; mar"
                        "gin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">Convert QRC</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">pyside6-rcc resources.qrc -o resources_rc.py</span></p></body></html>", None))
    # retranslateUi

