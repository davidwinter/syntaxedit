from qtpy import QtGui
from qtpy.QtWidgets import QTextEdit

from .highlightslot import HighlightSlot


class SyntaxEdit(QTextEdit):
    def __init__(
        self,
        content="",
        parent=None,
        font="Courier New",
        syntax="Markdown",
        theme="solarized-light",
        indentation_size=4,
        highlight_slot_class=HighlightSlot,
    ):
        super().__init__("", parent)

        self._indentation_size = indentation_size

        self.setFont(QtGui.QFont(font))
        self.setTabStopDistance(
            QtGui.QFontMetricsF(self.font()).horizontalAdvance(" ") * 4
        )

        self.setPlainText(content)

        self._syntax = syntax
        self._theme = theme

        self._highlight_slot = highlight_slot_class(self)

        self._highlight_text()

        self.textChanged.connect(self._highlight_slot.execute)

    def _highlight_text(self):
        self._highlight_slot.execute()

    def setSyntax(self, syntax):
        self._syntax = syntax
        self._highlight_text()

    def syntax(self):
        return self._syntax

    def theme(self):
        return self._theme

    def setTheme(self, theme):
        self._theme = theme
        self._highlight_text()

    def indentationSize(self):
        return self._indentation_size

    def editorFont(self):
        return self.currentFont().family()

    def cursorPosition(self):
        return self.textCursor().position()

    def setCursorPosition(self, position):
        cursor = self.textCursor()
        cursor.setPosition(position)
        self.setTextCursor(cursor)

    def setContents(self, contents):
        self.setPlainText(contents)
