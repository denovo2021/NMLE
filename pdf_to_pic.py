import fitz
from PIL import Image

# 01
# Specify input PDF file name and output directory
input_pdf = "/Users/Documents/TMDU/MedicalExaminationGPT/117/f_pic.pdf"
output_dir = "/Users/Documents/TMDU/MedicalExaminationGPT/117/f"

# Open PDF file
pdf = fitz.open(input_pdf)

# Create a scaling matrix
zoom_x = 2.0  # scale factor in x-direction
zoom_y = 2.0  # scale factor in y-direction
mat = fitz.Matrix(zoom_x, zoom_y)

for i in range(len(pdf)):
    page = pdf.load_page(i)
    # Convert the page to an image with increased resolution
    pix = page.get_pixmap(matrix=mat)
    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    output_filename = f"{output_dir}/page_{i+1}.jpg"
    # Save the image in JPEG format
    img.save(output_filename, "JPEG")

pdf.close()
