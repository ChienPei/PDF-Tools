import PyPDF2
import pdfplumber
import yaml

def extract_pages_based_on_text(source_pdf, target_pdf, text_criteria_list):
    pdf_reader = PyPDF2.PdfReader(source_pdf)
    pdf_writer = PyPDF2.PdfWriter()
    titles_of_pages = []

    with pdfplumber.open(source_pdf) as pdf:
        select_index = False
        for i, page in enumerate(pdf.pages):
            text = page.extract_text() if page.extract_text() else ""
            if any(criteria.lower() in text.lower() for criteria in text_criteria_list):
                select_index = True
            elif any(criteria.lower() in text.lower() for criteria in ['一']) and not any(criteria.lower() in text.lower() for criteria in text_criteria_list):
                select_index = False
            
            if select_index:
                for criteria in text_criteria_list:
                    if(criteria.lower() in text.lower()):
                        titles_of_pages.append(criteria)
                pdf_writer.add_page(pdf_reader.pages[i])

    with open(target_pdf, 'wb') as out_pdf:
        pdf_writer.write(out_pdf)

    return titles_of_pages

def main():
    with open("config.yaml", "r") as yamlfile:
        config = yaml.safe_load(yamlfile)

    source_pdf_path = config['source_pdf_path']
    target_pdf_path = config['target_pdf_path']
    text_criteria_list = config['text_criteria_list']

    titles_of_pages = extract_pages_based_on_text(source_pdf_path, target_pdf_path, text_criteria_list)
    print("Extracted Titles of Pages:", titles_of_pages)

if __name__ == "__main__":
    main()
