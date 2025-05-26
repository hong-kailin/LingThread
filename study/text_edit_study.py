from PySide6.QtWidgets import QApplication, QTextEdit
from PySide6.QtGui import QTextCursor, QTextCharFormat, QColor
import sys
import re

app = QApplication(sys.argv)
text_edit = QTextEdit()
text_edit.setPlainText("这是一段包含数字的文本：123，还有456和789。")

# 创建高亮格式
highlight_format = QTextCharFormat()
highlight_format.setBackground(QColor("lightgreen"))
highlight_format.setForeground(QColor("darkred"))

# 查找所有数字
selections = []
text = text_edit.toPlainText()
for match in re.finditer(r'\d+', text):
    start, end = match.span()

    # 创建光标并设置选中范围
    cursor = QTextCursor(text_edit.document())
    cursor.setPosition(start)
    cursor.setPosition(end, QTextCursor.KeepAnchor)

    # 创建额外选择区域
    selection = QTextEdit.ExtraSelection()
    selection.cursor = cursor
    selection.format = highlight_format
    selections.append(selection)

# 应用高亮
text_edit.setExtraSelections(selections)

text_edit.show()
sys.exit(app.exec())
