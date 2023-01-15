from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import get_lexer_by_name

from syntaxedit.highlightslot import HighlightSlot


class WidgetMock:
    def __init__(self, text=""):
        self.text = text
        self.html = ""
        self._cursorPosition = 5

    def cursorPosition(self):
        return self._cursorPosition

    def setCursorPosition(self, position):
        self._cursorPosition = position

    def syntax(self):
        return "Markdown"

    def theme(self):
        return "solarized-light"

    def editorFont(self):
        return "Courier New"

    def toPlainText(self):
        return self.text

    def toHtml(self):
        return self.html

    def setHtml(self, html):
        self.html = html

    def blockSignals(self, value):
        pass


def highlight_text(text):
    return highlight(
        text,
        get_lexer_by_name("Markdown", stripnl=False, ensurenl=False),
        HtmlFormatter(
            lineseparator="<br />",
            prestyles="white-space:pre-wrap; font-family: 'Courier New';",
            noclasses=True,
            nobackground=True,
            style="solarized-light",
        ),
    )


def test_text_highlighted():
    widget = WidgetMock("# Hello\n")
    slot = HighlightSlot(widget)

    slot.execute()

    assert widget.toHtml() == highlight_text("# Hello\n")
