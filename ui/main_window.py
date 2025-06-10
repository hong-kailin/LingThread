# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_main_window(object):
    def setupUi(self, main_window):
        if not main_window.objectName():
            main_window.setObjectName(u"main_window")
        main_window.resize(1005, 682)
        main_window.setMinimumSize(QSize(920, 530))
        main_window.setStyleSheet(u"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"#main_window{\n"
"	background-color:rgb(17, 45, 78);\n"
"}\n"
"#main_page, #project_list_page{\n"
"	background-color:rgb(37, 47, 82);\n"
"}\n"
"#bottom_line{\n"
"	background-color:rgb(63, 114, 175);\n"
"}\n"
"\n"
"#bottom_line QLabel { \n"
"	font-size: 11px; \n"
"	color: rgb(200, 200, 200); \n"
"	padding-left: 10px; \n"
"	padding-right: 10px; \n"
"	padding-bottom: 2px; \n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#left_sider_bar .QPushButton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#left_sider_bar .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#left_sider_bar .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"#top_line .QPushButton { background-color: rgba(255,"
                        " 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#top_line .QPushButton:hover { background-color: rgb(44, 49, 57); border-style: solid; border-radius: 4px; }\n"
"#top_line .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"#logo_label {\n"
"	background-image: url(:/images/images/images/LingThread_logo_42.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"\n"
"#left_title_label { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#left_description_label { font: 8pt \"Segoe UI\"; color: rgb(189, 147, 249); }\n"
"\n"
"\n"
"#main_page {\n"
"    background-image: url(:/images/images/images/LingThread_logo_382x369.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"}\n"
"\n"
"\n"
"")
        self.horizontalLayout = QHBoxLayout(main_window)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.left_sider_bar = QWidget(main_window)
        self.left_sider_bar.setObjectName(u"left_sider_bar")
        self.left_sider_bar.setMinimumSize(QSize(60, 0))
        self.left_sider_bar.setMaximumSize(QSize(60, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.left_sider_bar)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.left_sider_bar)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 50))
        self.widget.setMaximumSize(QSize(16777215, 50))
        self.logo_label = QLabel(self.widget)
        self.logo_label.setObjectName(u"logo_label")
        self.logo_label.setGeometry(QRect(10, 5, 42, 42))
        self.left_title_label = QLabel(self.widget)
        self.left_title_label.setObjectName(u"left_title_label")
        self.left_title_label.setGeometry(QRect(70, 5, 160, 20))
        self.left_description_label = QLabel(self.widget)
        self.left_description_label.setObjectName(u"left_description_label")
        self.left_description_label.setGeometry(QRect(70, 25, 160, 16))

        self.verticalLayout_2.addWidget(self.widget)

        self.hide_btn = QPushButton(self.left_sider_bar)
        self.hide_btn.setObjectName(u"hide_btn")
        self.hide_btn.setMinimumSize(QSize(60, 45))
        self.hide_btn.setMaximumSize(QSize(16777215, 16777215))
        self.hide_btn.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_menu.png);")
        self.hide_btn.setCheckable(True)
        self.hide_btn.setChecked(False)

        self.verticalLayout_2.addWidget(self.hide_btn)

        self.home_btn = QPushButton(self.left_sider_bar)
        self.home_btn.setObjectName(u"home_btn")
        self.home_btn.setMinimumSize(QSize(60, 45))
        self.home_btn.setMaximumSize(QSize(16777215, 16777215))
        self.home_btn.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-home.png);")

        self.verticalLayout_2.addWidget(self.home_btn)

        self.new_btn = QPushButton(self.left_sider_bar)
        self.new_btn.setObjectName(u"new_btn")
        self.new_btn.setMinimumSize(QSize(60, 45))
        self.new_btn.setMaximumSize(QSize(16777215, 16777215))
        self.new_btn.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-file.png);")

        self.verticalLayout_2.addWidget(self.new_btn)

        self.save_btn = QPushButton(self.left_sider_bar)
        self.save_btn.setObjectName(u"save_btn")
        self.save_btn.setMinimumSize(QSize(60, 45))
        self.save_btn.setMaximumSize(QSize(16777215, 16777215))
        self.save_btn.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-save.png)")

        self.verticalLayout_2.addWidget(self.save_btn)

        self.verticalSpacer = QSpacerItem(20, 250, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.about_btn = QPushButton(self.left_sider_bar)
        self.about_btn.setObjectName(u"about_btn")
        self.about_btn.setMinimumSize(QSize(60, 45))
        self.about_btn.setMaximumSize(QSize(16777215, 45))
        self.about_btn.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-arrow-right.png);")

        self.verticalLayout_2.addWidget(self.about_btn)


        self.horizontalLayout.addWidget(self.left_sider_bar)

        self.left_hide_box = QWidget(main_window)
        self.left_hide_box.setObjectName(u"left_hide_box")
        self.left_hide_box.setMaximumSize(QSize(0, 16777215))

        self.horizontalLayout.addWidget(self.left_hide_box)

        self.main_area = QWidget(main_window)
        self.main_area.setObjectName(u"main_area")
        self.verticalLayout = QVBoxLayout(self.main_area)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.top_line = QWidget(self.main_area)
        self.top_line.setObjectName(u"top_line")
        self.top_line.setMinimumSize(QSize(0, 45))
        self.top_line.setMaximumSize(QSize(16777215, 45))
        self.horizontalLayout_2 = QHBoxLayout(self.top_line)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 10, 0)
        self.label_2 = QLabel(self.top_line)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.horizontalSpacer = QSpacerItem(387, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.sentence_card_btn = QPushButton(self.top_line)
        self.sentence_card_btn.setObjectName(u"sentence_card_btn")
        self.sentence_card_btn.setMinimumSize(QSize(28, 28))
        self.sentence_card_btn.setMaximumSize(QSize(28, 28))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/cil-medical-cross.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.sentence_card_btn.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.sentence_card_btn)

        self.word_card_btn = QPushButton(self.top_line)
        self.word_card_btn.setObjectName(u"word_card_btn")
        self.word_card_btn.setMinimumSize(QSize(28, 28))
        self.word_card_btn.setMaximumSize(QSize(28, 28))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/cil-closed-captioning.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.word_card_btn.setIcon(icon1)
        self.word_card_btn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.word_card_btn)

        self.minimize_btn = QPushButton(self.top_line)
        self.minimize_btn.setObjectName(u"minimize_btn")
        self.minimize_btn.setMinimumSize(QSize(28, 28))
        self.minimize_btn.setMaximumSize(QSize(28, 28))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/cil-minus.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.minimize_btn.setIcon(icon2)
        self.minimize_btn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimize_btn)

        self.maximize_restore_btn = QPushButton(self.top_line)
        self.maximize_restore_btn.setObjectName(u"maximize_restore_btn")
        self.maximize_restore_btn.setMinimumSize(QSize(28, 28))
        self.maximize_restore_btn.setMaximumSize(QSize(28, 28))
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.maximize_restore_btn.setIcon(icon3)
        self.maximize_restore_btn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximize_restore_btn)

        self.close_app_btn = QPushButton(self.top_line)
        self.close_app_btn.setObjectName(u"close_app_btn")
        self.close_app_btn.setMinimumSize(QSize(28, 28))
        self.close_app_btn.setMaximumSize(QSize(28, 28))
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.close_app_btn.setIcon(icon4)
        self.close_app_btn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.close_app_btn)


        self.verticalLayout.addWidget(self.top_line)

        self.stacked_widget = QStackedWidget(self.main_area)
        self.stacked_widget.setObjectName(u"stacked_widget")
        self.main_page = QWidget()
        self.main_page.setObjectName(u"main_page")
        self.stacked_widget.addWidget(self.main_page)
        self.contents_page = QWidget()
        self.contents_page.setObjectName(u"contents_page")
        self.stacked_widget.addWidget(self.contents_page)
        self.project_list_page = QWidget()
        self.project_list_page.setObjectName(u"project_list_page")
        self.stacked_widget.addWidget(self.project_list_page)

        self.verticalLayout.addWidget(self.stacked_widget)

        self.bottom_line = QWidget(self.main_area)
        self.bottom_line.setObjectName(u"bottom_line")
        self.bottom_line.setMinimumSize(QSize(0, 20))
        self.bottom_line.setMaximumSize(QSize(16777215, 20))
        self.horizontalLayout_3 = QHBoxLayout(self.bottom_line)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.page_info = QLabel(self.bottom_line)
        self.page_info.setObjectName(u"page_info")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setBold(False)
        font.setItalic(False)
        self.page_info.setFont(font)

        self.horizontalLayout_3.addWidget(self.page_info)

        self.horizontalSpacer_2 = QSpacerItem(684, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.label_3 = QLabel(self.bottom_line)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.label_5 = QLabel(self.bottom_line)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(10, 10))
        self.label_5.setMaximumSize(QSize(10, 10))

        self.horizontalLayout_3.addWidget(self.label_5, 0, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignBottom)


        self.verticalLayout.addWidget(self.bottom_line)


        self.horizontalLayout.addWidget(self.main_area)


        self.retranslateUi(main_window)
        self.hide_btn.clicked["bool"].connect(main_window.show_hide_btn_name)
        self.maximize_restore_btn.clicked.connect(main_window.maximize_restore)
        self.close_app_btn.clicked.connect(main_window.close)
        self.minimize_btn.clicked.connect(main_window.showMinimized)
        self.about_btn.clicked.connect(main_window.show_hide_left_box)
        self.word_card_btn.clicked.connect(main_window.show_hide_word_card)
        self.sentence_card_btn.clicked.connect(main_window.show_hide_sentence_card)
        self.new_btn.clicked.connect(main_window.create_new_project)
        self.home_btn.clicked.connect(main_window.show_project_list)
        self.save_btn.clicked.connect(main_window.save_current_project_info)
        self.close_app_btn.clicked.connect(main_window.save_current_project_info)

        QMetaObject.connectSlotsByName(main_window)
    # setupUi

    def retranslateUi(self, main_window):
        main_window.setWindowTitle(QCoreApplication.translate("main_window", u"Form", None))
        self.logo_label.setText("")
        self.left_title_label.setText(QCoreApplication.translate("main_window", u"LingThread", None))
        self.left_description_label.setText(QCoreApplication.translate("main_window", u"English/Program", None))
        self.hide_btn.setText(QCoreApplication.translate("main_window", u"Hide", None))
        self.home_btn.setText(QCoreApplication.translate("main_window", u"Home", None))
        self.new_btn.setText(QCoreApplication.translate("main_window", u"New", None))
        self.save_btn.setText(QCoreApplication.translate("main_window", u"Save", None))
        self.about_btn.setText(QCoreApplication.translate("main_window", u"About", None))
        self.label_2.setText(QCoreApplication.translate("main_window", u"  LingThread - Learning is a process from disorder to order.", None))
        self.sentence_card_btn.setText("")
        self.word_card_btn.setText("")
        self.minimize_btn.setText("")
        self.maximize_restore_btn.setText("")
        self.close_app_btn.setText("")
        self.page_info.setText(QCoreApplication.translate("main_window", u"By: \u6bd4\u98de\u9e1f\u8d35\u91cd\u7684\u591a_HKL", None))
        self.label_3.setText(QCoreApplication.translate("main_window", u"v1.0.0", None))
        self.label_5.setText("")
    # retranslateUi

