from ui import Ui_styleSheet
from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QIcon
from PySide6.QtCore import QEvent, QTimer


class StyleSheet(QWidget, Ui_styleSheet):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.titleRightInfo.installEventFilter(self)
        # CLOSE APPLICATION
        self.closeAppBtn.clicked.connect(lambda: self.close())

    def eventFilter(self, obj, event):
        if obj == self.titleRightInfo and event.type() == QEvent.MouseButtonDblClick:
            QTimer.singleShot(250, self.maximize_restore)
            return True
        return super().eventFilter(obj, event)

    def maximize_restore(self):
        main_window = self.window()
        if not main_window.isMaximized():
            main_window.showMaximized()
            self.appMargins.setContentsMargins(0, 0, 0, 0)
            self.maximizeRestoreAppBtn.setToolTip("Restore")
            self.maximizeRestoreAppBtn.setIcon(QIcon(u":/icons/images/icons/icon_restore.png"))
            self.frame_size_grip.hide()
            # self.left_grip.hide()
            # self.right_grip.hide()
            # self.top_grip.hide()
            # self.bottom_grip.hide()
        else:
            main_window = self.window()
            main_window.showNormal()
            self.resize(self.width() + 1, self.height() + 1)
            self.appMargins.setContentsMargins(10, 10, 10, 10)
            self.maximizeRestoreAppBtn.setToolTip("Maximize")
            self.maximizeRestoreAppBtn.setIcon(QIcon(u":/icons/images/icons/icon_maximize.png"))
            self.frame_size_grip.show()
            # self.left_grip.show()
            # self.right_grip.show()
            # self.top_grip.show()
            # self.bottom_grip.show()
