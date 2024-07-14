import streamlit as st
import fitz  # PyMuPDF
from PIL import Image
import io

st.title('PDF to Images Converter')

# Drag and drop box for PDF file
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    # Read the PDF file
    pdf_document = fitz.open(stream=uploaded_file.read(), filetype="pdf")

    st.write(f"Number of pages: {pdf_document.page_count}")

    images = []

    # Iterate through each page and convert to image
    for page_num in range(pdf_document.page_count):
        page = pdf_document.load_page(page_num)
        pix = page.get_pixmap()
        
        # Convert to image using PIL
        img = Image.open(io.BytesIO(pix.tobytes("png")))
        images.append(img)

    # Display images
    st.write("### PDF Pages as Images")
    for img in images:
        st.image(img)
