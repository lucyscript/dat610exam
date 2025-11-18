#!/usr/bin/env python3
"""
Script to split Lecture10-IoT.pdf into smaller parts
Similar to how Lecture6-CellularNetworks was split
"""

import PyPDF2
import sys
import os

def split_pdf(input_pdf, output_prefix, pages_per_part=30):
    """
    Split a PDF into multiple parts

    Args:
        input_pdf: Path to input PDF file
        output_prefix: Prefix for output files
        pages_per_part: Number of pages per output file
    """
    try:
        # Open the PDF
        with open(input_pdf, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            total_pages = len(pdf_reader.pages)

            print(f"Total pages in {input_pdf}: {total_pages}")
            print(f"Splitting into parts of {pages_per_part} pages each...")

            # Calculate number of parts needed
            num_parts = (total_pages + pages_per_part - 1) // pages_per_part

            for part_num in range(num_parts):
                # Create a new PDF writer for this part
                pdf_writer = PyPDF2.PdfWriter()

                # Calculate page range for this part
                start_page = part_num * pages_per_part
                end_page = min(start_page + pages_per_part, total_pages)

                # Add pages to this part
                for page_num in range(start_page, end_page):
                    pdf_writer.add_page(pdf_reader.pages[page_num])

                # Write the output file
                output_filename = f"{output_prefix}_part{part_num + 1}.pdf"
                with open(output_filename, 'wb') as output_file:
                    pdf_writer.write(output_file)

                print(f"Created {output_filename} (pages {start_page + 1}-{end_page})")

            print(f"\nSuccessfully split into {num_parts} parts!")

    except FileNotFoundError:
        print(f"Error: File '{input_pdf}' not found!")
        sys.exit(1)
    except Exception as e:
        print(f"Error splitting PDF: {e}")
        sys.exit(1)

if __name__ == "__main__":
    input_file = "/home/user/dat610exam/Lecture10-IoT.pdf"
    output_prefix = "/home/user/dat610exam/Lecture10-IoT"

    # Split into parts of 30 pages each (adjust if needed)
    split_pdf(input_file, output_prefix, pages_per_part=30)
