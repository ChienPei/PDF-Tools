import sys
from PyPDF2 import PdfReader, PdfWriter

def remove_pdf_pages(file_path, pages_to_remove, output_file_path):
    """
    Remove specific pages from a PDF.
    Parameters:
    - file_path: The path of the input PDF file.
    - pages_to_remove: A list of page numbers to remove (1-indexed).
    - output_file_path: The path of the output PDF file after removing pages.
    """
    
    pages_to_remove = [x - 1 for x in pages_to_remove]
    print(f"Removing pages: {pages_to_remove}")

    # Load PDF
    with open(file_path, 'rb') as file:
        reader = PdfReader(file)
        writer = PdfWriter()
        
        # Add all pages except the ones to remove
        for page_num in range(len(reader.pages)):
            if page_num not in pages_to_remove:
                writer.add_page(reader.pages[page_num])
        
        # Save the result to a new file
        with open(output_file_path, 'wb') as output_file:
            writer.write(output_file)


def main():
    if len(sys.argv) != 4:
        print("Usage: python script.py input_pdf pages_to_remove output_pdf")
        sys.exit(1)

    input_pdf = sys.argv[1]
    pages_to_remove = list(map(int, sys.argv[2].split(',')))
    output_pdf = sys.argv[3]

    remove_pdf_pages(input_pdf, pages_to_remove, output_pdf)

if __name__ == "__main__":
    main()