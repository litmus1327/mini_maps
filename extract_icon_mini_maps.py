import os
import fitz  # PyMuPDF

def extract_mini_maps():
    # Find the PDF file in the current directory containing 'Door Location Summary'
    pdf_files = [f for f in os.listdir('.') if f.lower().endswith('.pdf') and 'door location summary' in f.lower()]
    if not pdf_files:
        print("No 'Door Location Summary' PDF found in current folder.")
        return
    pdf_path = pdf_files[0]
    print(f"Using PDF: {pdf_path}")

    # Extract facility name (everything before first ' -' or first '-')
    facility_name = pdf_path.split(' -')[0].split('-')[0].strip().replace(' ', '')

    output_dir = f"{facility_name}_MiniMaps_Final"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    doc = fitz.open(pdf_path)
    print("Extracting and cropping mini maps...")

    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text_instances = page.search_for("Icon")

        for inst_num, inst in enumerate(text_instances, start=1):
            images = page.get_images(full=True)

            found = False
            for img in images:
                xref = img[0]
                rects = page.get_image_rects(xref)
                if not rects:
                    continue
                rect = rects[0]

                # Check if image is to the right of "Icon" text and roughly vertically aligned
                if rect.x0 > inst.x1 and abs(rect.y0 - inst.y0) < 100:
                    # Padding settings
                    horizontal_pad = 74
                    vertical_pad = 64

                    crop_rect = fitz.Rect(
                        max(rect.x0 - horizontal_pad, 0),
                        max(rect.y0 - vertical_pad, 0),
                        rect.x1 + horizontal_pad,
                        rect.y1 + vertical_pad,
                    )

                    zoom = 4.0
                    mat = fitz.Matrix(zoom, zoom)

                    cropped_pix = page.get_pixmap(matrix=mat, clip=crop_rect)

                    out_name = f"{facility_name}_Icon{page_num + 1}_{inst_num}.png"
                    out_path = os.path.join(output_dir, out_name)
                    cropped_pix.save(out_path)
                    print(f"Saved cropped mini map: {out_name}")

                    found = True
                    break  # Only save first matching image per "Icon" instance
            if not found:
                print(f"Warning: No matching image found for Icon on page {page_num + 1}, instance {inst_num}")

    print(f"\n🎉 All mini maps cropped and saved in {output_dir}")

    # Save output folder name for next script
    with open("last_output_folder.txt", "w") as f:
        f.write(output_dir)

if __name__ == "__main__":
    extract_mini_maps()
