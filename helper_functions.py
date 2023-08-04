import os
from PIL import Image
from reportlab.pdfgen import canvas

def create_new_directory(directory_path):

    if not os.path.exists(directory_path):
        try:
            os.makedirs(directory_path)
        except OSError as e:
            print(f"Error creating directory: {e}")


def generate_pdf_with_text_content(file_path, pdf_content, pagesize, font_name, font_size):

    pdf_handle = canvas.Canvas(file_path, pagesize=pagesize)

    # Set the font and font size
    pdf_handle.setFont("Helvetica", font_size)

    pdf_handle.drawString(72, 800, pdf_content.encode('utf-8'))

    return pdf_handle

def generate_pdf_with_picture(file_path, path_picture, pagesize):
    # Load the image
    
    pdf_handle = canvas.Canvas(file_path)

    image = Image.open(path_picture)
    image_width, image_height = image.size

    # Scale the image to fit the page width (keeping the aspect ratio)
    page_width, page_height = pagesize
    scale_factor = min(page_width / image_width, page_height / image_height)
    image_width *= scale_factor
    image_height *= scale_factor

    # Calculate the position to center the image on the page
    x_offset = (page_width - image_width) / 2
    y_offset = (page_height - image_height) / 2

    # Draw the image on the PDF canvas
    pdf_handle.drawInlineImage(path_picture, x_offset, y_offset, width=image_width, height=image_height)

    return pdf_handle