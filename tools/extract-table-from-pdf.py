#!/usr/bin/env python
import pdfplumber
import argparse
import csv

def parse_page_range(value):
    parsed_range = set()
    for part in value.split(','):
        if '-' in part:
            start, end = map(int, part.split('-'))
            parsed_range.update(range(start, end + 1))
        else:
            parsed_range.add(int(part))
    return sorted(parsed_range)

def extract_tables(pdf_path, page_num):
    output_csv = f'extracted-csv_page-{page_num}.csv'
    with pdfplumber.open(pdf_path) as pdf:
        try:
            page = pdf.pages[page_num - 1]  # page numbering starts at 1
        except IndexError:
            print(f"Page {page_num} does not exist in the PDF.")
            return
               
        tables = page.extract_tables(
            table_settings = {
                'vertical_strategy': 'text',
                'horizontal_strategy': 'lines'
            }
        )
        if not tables:
            print(f"No tables found on page {page_num}.")
            return

        table = tables[0]
        with open(output_csv, 'w', newline='') as f:
            writer = csv.writer(f)
            for row in table:
                cleaned_row = []
                for cell in row:
                    # Check if cell is not None to avoid errors
                    if cell is not None:
                        # Remove newlines and extra spaces
                        cell = cell.replace('\n', ' ').strip()
                    cleaned_row.append(cell)
                writer.writerow(cleaned_row)
        print(f"Table extracted and saved to {output_csv}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Extract a table from a PDF using pdfplumber"
    )
    parser.add_argument("pdf_path", help="Path to the PDF file")
    parser.add_argument(
        "--page", type=parse_page_range, default=[1], help='Page numbers or ranges (e.g., "1-5,12,18")'
    )
    args = parser.parse_args()
    
    for page in args.page:
        extract_tables(args.pdf_path, page)
