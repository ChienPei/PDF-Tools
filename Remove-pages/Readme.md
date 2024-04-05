# PDF Page Remover Tool

This Python script allows users to remove specific pages from a PDF document.

## Features

- Remove specified pages from any PDF file.
- Simple command-line interface.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- You have installed Python 3.x
- You have installed the PyPDF2 library

## Usage
To use the PDF Page Remover tool, follow these steps:
```bash
python3 pages_remover.py input.pdf "1,2,5" output.pdf
```
Where input.pdf is the file path to your PDF, "1,2,5" is a comma-separated list of page numbers to be removed (1-indexed), and output.pdf is the desired output file name.

## Contributing
Your contributions are always welcome! If you have any improvements or ideas, please feel free to fork the repository and submit a pull request.