# PDF Text-Based Extraction Tool

This tool automates the extraction of pages from a PDF file based on specific text criteria. It is ideal for segregating sections or chapters of interest from larger documents. The tool scans through each page of a source PDF, matches pages against a predefined list of text criteria, and then extracts those pages into a new PDF document. Additionally, it captures the titles (or any specified text criteria) from the extracted pages for further reference or processing.

## Features

- Extract pages from a PDF based on text criteria.
- Support for multiple text criteria.
- Outputs a new PDF with only the pages that match the criteria.
- Lists titles or specified text from the extracted pages.

## Requirements

To use this tool, you will need Python installed on your system along with the following Python packages:

- PyPDF2
- pdfplumber
- PyYAML

You can install these packages using pip:

```bash
pip install PyPDF2 pdfplumber PyYAML
```
## Configuration
Update the paths and criteria list in `config.yaml` to match your requirements.
```yaml
source_pdf_path: 'path/to/source.pdf'
target_pdf_path: 'path/to/target.pdf'
text_criteria_list:
  - 'Text Criteria 1'
  - 'Text Criteria 2'
  ... 
```
## Usage
To run the script, execute the following command in the terminal:
```bash
python3 text_page_extractor.py
```

This will extract pages from source_pdf_path containing the text defined in text_criteria_list and save them to target_pdf_path.

## Output
The script will print out the titles of pages extracted based on the specified text criteria. These titles are the text criteria found on each extracted page.

## Contributing
Your contributions are always welcome! If you have any improvements or ideas, please feel free to fork the repository and submit a pull request.
