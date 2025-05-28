# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'project_widget_list.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QListWidget, QListWidgetItem,
    QSizePolicy, QWidget)

class Ui_project_list(object):
    def setupUi(self, project_list):
        if not project_list.objectName():
            project_list.setObjectName(u"project_list")
        project_list.resize(400, 300)
        project_list.setStyleSheet(u"#project_list, #project_widget_list {\n"
"    background-color: transparent;\n"
"}")
        self.horizontalLayout = QHBoxLayout(project_list)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.project_widget_list = QListWidget(project_list)
        self.project_widget_list.setObjectName(u"project_widget_list")

        self.horizontalLayout.addWidget(self.project_widget_list)


        self.retranslateUi(project_list)

        QMetaObject.connectSlotsByName(project_list)
    # setupUi

    def retranslateUi(self, project_list):
        project_list.setWindowTitle(QCoreApplication.translate("project_list", u"Form", None))
    # retranslateUi

