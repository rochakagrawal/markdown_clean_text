# Markdown to HTML Clipboard Converter (without HTML tags, Rich Text format)

This Python script converts Markdown text from your clipboard to HTML (Rich Text format, **without html tags**), preserving formatting when pasting into rich text applications like Microsoft Word or Apple Pages or Microsoft OneNote.

While it's relatively easy to convert Markdown to HTML, you won't be able to simply paste the text into MS Word or Apple Notes, as they can't render the HTML. This special script allows you to do just that. If you love it, please say that in comments.

## Features

- Converts Markdown to HTML using Pandoc Rich Text format, **without html tags**),
- Automatically detects if clipboard content is likely Markdown
- Places converted HTML directly on the clipboard for easy pasting
- Works on macOS

## Requirements

- Python 3.6+
- macOS (due to use of AppKit)
- Pandoc

## Installation

1. Clone this repository (download the single python file)
2. Install the required Python packages:**pip install pypandoc pyperclip pyobjc**
3. Install Pandoc (if not already installed):**brew install pandoc**

## Usage

1. Copy your Markdown text to the clipboard.
2. Run the script:**python markdown_to_rtf.py**
3. The script will convert the Markdown to HTML and place it on your clipboard.
4. Paste the converted content into your desired application (e.g., MS Word, Apple Pages).
- Use "Paste and Match Style" or similar options for best results.

## How It Works

1. The script checks if the clipboard content is likely Markdown.
2. If it is, it uses Pandoc to convert the Markdown to HTML.
3. The resulting HTML is placed on the clipboard using macOS's AppKit.
4. You can then paste the formatted content into your application of choice.

## Raycast Script
I love raycast so I am using this python script as my raycast script. It's super easy to first copy the markdown text in my clipboard, run this script on raycast using keyboard, and have the formatted output in my clipboard to paste

## Video

https://youtu.be/044KqR8irZA

## Limitations

- Currently only works on macOS due to the use of AppKit for clipboard operations.
- The Markdown detection is based on common patterns and may not catch all valid Markdown or may incorrectly identify some non-Markdown text.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Pandoc](https://pandoc.org/) for Markdown to HTML conversion
- [pyperclip](https://pypi.org/project/pyperclip/) for cross-platform clipboard operations
- [pyobjc](https://pypi.org/project/pyobjc/) for macOS-specific functionality
