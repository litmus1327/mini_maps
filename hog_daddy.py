import os
import re
from PyPDF2 import PdfReader
from PIL import Image

def find_pdf_with_keyword(keyword="Door Location"):
    # Search current directory for a PDF containing the keyword in its filename
    for filename in os.listdir('.'):
        if filename.lower().endswith('.pdf') and keyword.lower() in filename.lower():
            return filename
    return None

def extract_mini_maps_from_pdf(pdf_path):
    print(f"Using PDF: {pdf_path}")
    reader = PdfReader(pdf_path)

    # Extract facility name from PDF filename: part to the left of first hyphen
    base_name = os.path.splitext(os.path.basename(pdf_path))[0]
    if '-' in base_name:
        facility_name = base_name.split('-')[0].strip()
    else:
        facility_name = base_name
    # Sanitize folder name to remove any unwanted characters
    facility_name = re.sub(r'[^A-Za-z0-9]', '', facility_name)

    output_folder = f"{facility_name}_MiniMaps_Final"
    os.makedirs(output_folder, exist_ok=True)

    for page_num, page in enumerate(reader.pages):
        text = page.extract_text()
        if not text:
            continue

        # Find all occurrences of "Icon" with their numbers
        icon_matches = list(re.finditer(r'Icon\s*(\d+)', text))
        if not icon_matches:
            continue

        for idx, match in enumerate(icon_matches):
            icon_num = match.group(1)

            # Here replace with your actual mini map image extraction and cropping logic
            filename = f"{icon_num}.png"

            # Placeholder image creation (replace with real extraction)
            img = Image.new('RGB', (400, 300), color='gray')
            img.save(os.path.join(output_folder, filename))
            print(f"Saved mini map: {filename}")

    print(f"\nAll mini maps saved to folder: {output_folder}")
    return output_folder

def main():
    pdf_file = find_pdf_with_keyword()
    if not pdf_file:
        print("No PDF file containing 'Door Location' found in current folder.")
        return

    output_folder = extract_mini_maps_from_pdf(pdf_file)
    # Additional logic like git push can be added here

if __name__ == "__main__":
    main()
