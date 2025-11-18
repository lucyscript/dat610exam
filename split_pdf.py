#!/usr/bin/env python3
"""Split a large PDF into smaller chunks."""
import os
from PyPDF2 import PdfReader, PdfWriter

def split_pdf(input_pdf, pages_per_chunk=50):
    """Split PDF into chunks of specified page count."""
    reader = PdfReader(input_pdf)
    total_pages = len(reader.pages)

    print(f"Total pages in {input_pdf}: {total_pages}")

    base_name = os.path.splitext(input_pdf)[0]

    chunk_num = 1
    for start_page in range(0, total_pages, pages_per_chunk):
        end_page = min(start_page + pages_per_chunk, total_pages)

        writer = PdfWriter()
        for page_num in range(start_page, end_page):
            writer.add_page(reader.pages[page_num])

        output_filename = f"{base_name}_part{chunk_num}.pdf"
        with open(output_filename, 'wb') as output_file:
            writer.write(output_file)

        print(f"Created {output_filename} (pages {start_page + 1}-{end_page})")
        chunk_num += 1

    print(f"\nSplit complete! Created {chunk_num - 1} parts.")

if __name__ == "__main__":
    split_pdf("Lecture6-CellularNetworks.pdf", pages_per_chunk=50)
