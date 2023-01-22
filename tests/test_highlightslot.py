from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import get_lexer_by_name

from syntaxedit.highlightslot import HighlightSlot


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


def test_text_highlighted(mocker):
    widget = mocker.MagicMock()
    widget.syntax.return_value = "Markdown"
    widget.theme.return_value = "solarized-light"
    widget.editorFont.return_value = "Courier New"
    widget.toPlainText.return_value = "# Hello\n"

    slot = HighlightSlot(widget)
    slot.execute()

    widget.setHtml.assert_called_once_with(highlight_text("# Hello\n"))
