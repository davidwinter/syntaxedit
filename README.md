# syntaxedit

[![test](https://github.com/davidwinter/syntaxedit/workflows/ci_cd/badge.svg)](https://github.com/davidwinter/syntaxedit/actions?query=workflow%3Aci_cd) [![PyPI](https://img.shields.io/pypi/v/syntaxedit)](https://pypi.org/project/syntaxedit/)

> A simple Python Qt syntax highlighting widget

![syntaxedit](https://raw.githubusercontent.com/davidwinter/syntaxedit/main/example.png)

## Features

- Extensive [syntax](https://pygments.org/languages/) and [theme](https://pygments.org/styles/) support - powered by [Pygments](https://pygments.org)
- Set font and font size
- Set indentation size

## Usage

1. Install package

   ```shell
   pip install syntaxedit
   ```

   Or

   ```shell
   poetry add syntaxedit
   ```

2. In your app, include the package, and create a `SyntaxEdit` widget:

    ```python
    from syntaxedit.core import SyntaxEdit

    code = """# Todo list

    - [ ] Go shopping
    - [x] Walk the dog"""

    widget = SyntaxEdit(code)
    ```

### Available options

- `content`: the initial content for the widget. **Default:** `""`
- `parent`: parent Qt widget for SyntaxEdit. **Default:** `None`
- `font`: the font family for the widget. **Default:** `"Courier New"`
- `font_size`: size to use for the font. **Default:** `13`
- `syntax`: the code [syntax](https://pygments.org/languages/) to use. **Default:** `"Markdown"`
- `theme`: the syntax [theme](https://pygments.org/styles/) to use. **Default:** `"solarized-light"`
- `indentation_size`: the size for indentation. **Default:** `4`

## Authors

By [David Winter](https://github.com/davidwinter)

## License

MIT
