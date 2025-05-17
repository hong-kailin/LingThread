# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_main_window(object):
    def setupUi(self, main_window):
        if not main_window.objectName():
            main_window.setObjectName(u"main_window")
        main_window.resize(964, 572)
        main_window.setMinimumSize(QSize(920, 530))
        main_window.setStyleSheet(u"")
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
        self.label = QLabel(self.left_sider_bar)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(60, 45))
        self.label.setMaximumSize(QSize(60, 45))

        self.verticalLayout_2.addWidget(self.label)

        self.pushButton = QPushButton(self.left_sider_bar)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(60, 45))
        self.pushButton.setMaximumSize(QSize(60, 45))

        self.verticalLayout_2.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.left_sider_bar)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(60, 45))
        self.pushButton_2.setMaximumSize(QSize(60, 45))

        self.verticalLayout_2.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.left_sider_bar)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(60, 45))
        self.pushButton_3.setMaximumSize(QSize(60, 45))

        self.verticalLayout_2.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.left_sider_bar)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(60, 45))
        self.pushButton_4.setMaximumSize(QSize(60, 45))

        self.verticalLayout_2.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.left_sider_bar)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(60, 45))
        self.pushButton_5.setMaximumSize(QSize(60, 45))

        self.verticalLayout_2.addWidget(self.pushButton_5)

        self.verticalSpacer = QSpacerItem(20, 254, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.pushButton_6 = QPushButton(self.left_sider_bar)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(60, 45))
        self.pushButton_6.setMaximumSize(QSize(60, 45))

        self.verticalLayout_2.addWidget(self.pushButton_6)


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
        self.widget_4 = QWidget(self.main_area)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMinimumSize(QSize(0, 45))
        self.widget_4.setMaximumSize(QSize(16777215, 45))
        self.horizontalLayout_2 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 10, 0)
        self.label_2 = QLabel(self.widget_4)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.horizontalSpacer = QSpacerItem(389, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.pushButton_7 = QPushButton(self.widget_4)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(28, 28))
        self.pushButton_7.setMaximumSize(QSize(28, 28))

        self.horizontalLayout_2.addWidget(self.pushButton_7)

        self.pushButton_8 = QPushButton(self.widget_4)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(28, 28))
        self.pushButton_8.setMaximumSize(QSize(28, 28))

        self.horizontalLayout_2.addWidget(self.pushButton_8)

        self.pushButton_9 = QPushButton(self.widget_4)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMinimumSize(QSize(28, 28))
        self.pushButton_9.setMaximumSize(QSize(28, 28))

        self.horizontalLayout_2.addWidget(self.pushButton_9)

        self.pushButton_10 = QPushButton(self.widget_4)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setMinimumSize(QSize(28, 28))
        self.pushButton_10.setMaximumSize(QSize(28, 28))

        self.horizontalLayout_2.addWidget(self.pushButton_10)


        self.verticalLayout.addWidget(self.widget_4)

        self.widget_5 = QWidget(self.main_area)
        self.widget_5.setObjectName(u"widget_5")

        self.verticalLayout.addWidget(self.widget_5)

        self.widget_6 = QWidget(self.main_area)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMinimumSize(QSize(0, 20))
        self.widget_6.setMaximumSize(QSize(16777215, 20))
        self.horizontalLayout_3 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.widget_6)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.horizontalSpacer_2 = QSpacerItem(715, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.label_3 = QLabel(self.widget_6)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.label_5 = QLabel(self.widget_6)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(10, 10))
        self.label_5.setMaximumSize(QSize(10, 10))

        self.horizontalLayout_3.addWidget(self.label_5, 0, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignBottom)


        self.verticalLayout.addWidget(self.widget_6)


        self.horizontalLayout.addWidget(self.main_area)


        self.retranslateUi(main_window)

        QMetaObject.connectSlotsByName(main_window)
    # setupUi

    def retranslateUi(self, main_window):
        main_window.setWindowTitle(QCoreApplication.translate("main_window", u"Form", None))
        self.label.setText(QCoreApplication.translate("main_window", u"TextLabel", None))
        self.pushButton.setText(QCoreApplication.translate("main_window", u"Hide", None))
        self.pushButton_2.setText(QCoreApplication.translate("main_window", u"Home", None))
        self.pushButton_3.setText(QCoreApplication.translate("main_window", u"New", None))
        self.pushButton_4.setText(QCoreApplication.translate("main_window", u"Save", None))
        self.pushButton_5.setText(QCoreApplication.translate("main_window", u"Exit", None))
        self.pushButton_6.setText(QCoreApplication.translate("main_window", u"About", None))
        self.label_2.setText(QCoreApplication.translate("main_window", u"  LingThread - Learning is a process from disorder to order.", None))
        self.pushButton_7.setText("")
        self.pushButton_8.setText("")
        self.pushButton_9.setText("")
        self.pushButton_10.setText("")
        self.label_4.setText(QCoreApplication.translate("main_window", u"By: \u6bd4\u98de\u9e1f\u8d35\u91cd\u7684\u591a_HKL", None))
        self.label_3.setText(QCoreApplication.translate("main_window", u"v1.0.0", None))
        self.label_5.setText("")
    # retranslateUi

