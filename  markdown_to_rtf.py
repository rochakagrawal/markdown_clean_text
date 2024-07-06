#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Markdown-to-Clean-Text
# @raycast.mode fullOutput

# Optional parameters:
# @raycast.icon 🧹

# Documentation:
# @raycast.description Convert Markdown to clean text
# @raycast.author Rochak Agrawal
# @raycast.authorURL https://raycast.com/YourName

import pypandoc
import pyperclip
from AppKit import NSPasteboard, NSPasteboardTypeHTML
import re

def is_likely_markdown(text):
    # Check for common Markdown syntax
    markdown_patterns = [
        r'^#{1,6}\s',  # Headers
        r'(\*\*|__).+?(\*\*|__)',  # Bold
        r'(\*|_).+?(\*|_)',  # Italic
        r'^\s*[-*+]\s',  # Unordered lists
        r'^\s*\d+\.\s',  # Ordered lists
        r'^\s*>\s',  # Blockquotes
        r'`{1,3}.*?`{1,3}',  # Code (inline or block)
        r'\[.+?\]\(.+?\)',  # Links
        r'!\[.+?\]\(.+?\)',  # Images
        r'^-{3,}$',  # Horizontal rules
    ]
    
    for pattern in markdown_patterns:
        if re.search(pattern, text, re.MULTILINE):
            return True
    return False

def convert_markdown_to_html(markdown_text):
    # Convert Markdown to HTML
    html = pypandoc.convert_text(markdown_text, 'html', format='markdown-raw_html')
    return html

def set_clipboard_html(html_text):
    pb = NSPasteboard.generalPasteboard()
    pb.clearContents()
    pb.setString_forType_(html_text, NSPasteboardTypeHTML)

def main():
    # Get text from the clipboard
    clipboard_text = pyperclip.paste()
    if not clipboard_text:
        print("No text found in clipboard.")
        return

    # Check if the text is likely Markdown
    if not is_likely_markdown(clipboard_text):
        print("The clipboard content doesn't appear to be Markdown.")
        print("Please ensure you've copied Markdown text before running this script.")
        return

    # Convert to HTML
    html_text = convert_markdown_to_html(clipboard_text)

    # Set HTML text to clipboard
    set_clipboard_html(html_text)
    
    print("Converted HTML text has been copied to the clipboard.")
    print("You can now paste the formatted content into your desired application (e.g., MS Word, Apple Pages, etc.).")
    print("Please use 'Paste and Match Style' or similar option if available.")

if __name__ == "__main__":
    main()