from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import get_lexer_by_name
from qtpy import QtGui
from qtpy.QtWidgets import QTextEdit


class SyntaxEdit(QTextEdit):
    def __init__(
        self,
        content="",
        parent=None,
        font="Courier New",
        language="Markdown",
        style="solarized-light",
    ):
        super().__init__("", parent)

        self._font = font

        new_font = QtGui.QFont(self._font)
        self.setFont(new_font)
        self.setTabStopDistance(
            QtGui.QFontMetricsF(self.font()).horizontalAdvance(" ") * 4
        )

        self.setPlainText(content)

        self._language = language
        self._style = style

        self._highlight_text()

        self.textChanged.connect(self._highlight_text)

    def setLanguage(self, language):
        self._language = language
        self._highlight_text()

    def language(self):
        return self._language

    def style(self):
        return self._style

    def setStyle(self, style):
        self._style = style
        self._highlight_text()

    def setContents(self, contents):
        self.setPlainText(contents)

    def _highlight_text(self):
        markup = highlight(
            self.toPlainText(),
            get_lexer_by_name(self.language(), stripnl=False, ensurenl=False),
            HtmlFormatter(
                lineseparator="<br />",
                prestyles=f"white-space:pre-wrap; font-family: '{self._font}';",
                noclasses=True,
                nobackground=True,
                style=self.style(),
            ),
        )

        position = self.textCursor().position()

        self.blockSignals(True)
        self.setHtml(markup)
        self.blockSignals(False)

        cursor = self.textCursor()
        cursor.setPosition(position)
        self.setTextCursor(cursor)
