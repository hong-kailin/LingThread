import sys
from page import MainWindowPage, LeftBoxPage, NewDialogPage
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindowPage()

    v_layout = QVBoxLayout(window.left_hide_box)
    v_layout.setContentsMargins(0, 0, 0, 0)
    left_box = LeftBoxPage()
    v_layout.addWidget(left_box)
    left_box.close_left_box_signal.connect(window.show_hide_left_box)

    def create_new_english_note():
        new_window = NewDialogPage(window)
        if new_window.exec():
            print("===")

    window.create_new_english_note_signal.connect(create_new_english_note)
    window.show()
    app.exec()
