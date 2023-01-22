import pytest

from qtpy import QtGui

from syntaxedit.core import SyntaxEdit


@pytest.fixture(autouse=True)
def mock_highlightslot(mocker):
    return mocker.patch("syntaxedit.core.HighlightSlot")


def test_constructor_defaults(qtbot):
    widget = SyntaxEdit()

    assert widget.syntax() == "Markdown"
    assert widget.theme() == "solarized-light"
    assert widget.indentationSize() == 4
    assert widget.editorFont() == "Courier New"

    assert widget.toPlainText() == ""


def test_constructor_overrides(qtbot):
    widget = SyntaxEdit(
        "Hello",
        syntax="HTML",
        theme="solarized-dark",
        font="Arial",
        indentation_size=2,
    )

    assert widget.syntax() == "HTML"
    assert widget.theme() == "solarized-dark"
    assert widget.indentationSize() == 2
    assert widget.currentFont().family() == "Arial"

    assert widget.toPlainText() == "Hello"


def test_indentation_size(qtbot):
    widget = SyntaxEdit()

    tab_size = (
        QtGui.QFontMetricsF(widget.currentFont()).horizontalAdvance(" ")
        * widget.indentationSize()
    )

    assert widget.tabStopDistance() == tab_size


def test_textchanged_signal_connected(qtbot, mock_highlightslot):
    instance = mock_highlightslot.return_value

    widget = SyntaxEdit()
    widget.setPlainText("hello")

    assert instance.execute.call_count == 2
