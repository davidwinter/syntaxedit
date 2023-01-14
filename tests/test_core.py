from qtpy import QtGui

from syntaxedit.core import SyntaxEdit


class HighlightSlotMock:
    def __init__(self, widget):
        self.widget = widget
        self.call_count = 0

    def execute(self):
        self.call_count += 1


def test_constructor_defaults(qtbot):
    widget = SyntaxEdit(highlight_slot_class=HighlightSlotMock)

    assert widget.syntax() == "Markdown"
    assert widget.theme() == "solarized-light"
    assert widget.indentationSize() == 4
    assert widget.editorFont() == "Courier New"
    # assert widget._highlight_slot.__class__.__name__ == "HighlightSlot"

    assert widget.toPlainText() == ""


def test_constructor_overrides(qtbot):
    widget = SyntaxEdit(
        "Hello",
        syntax="HTML",
        theme="solarized-dark",
        font="Arial",
        indentation_size=2,
        highlight_slot_class=HighlightSlotMock,
    )

    assert widget.syntax() == "HTML"
    assert widget.theme() == "solarized-dark"
    assert widget.indentationSize() == 2
    assert widget.currentFont().family() == "Arial"
    assert widget._highlight_slot.__class__.__name__ == "HighlightSlotMock"

    assert widget.toPlainText() == "Hello"


def test_textchanged_signal_connected(qtbot):
    widget = SyntaxEdit(highlight_slot_class=HighlightSlotMock)

    widget.setPlainText("hello")

    assert widget._highlight_slot.call_count == 2


def test_indentation_size(qtbot):
    widget = SyntaxEdit(highlight_slot_class=HighlightSlotMock)

    tab_size = (
        QtGui.QFontMetricsF(widget.currentFont()).horizontalAdvance(" ")
        * widget.indentationSize()
    )

    assert widget.tabStopDistance() == tab_size
