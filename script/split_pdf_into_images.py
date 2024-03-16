"""
Given a pdf file, SPLIT it into images
TODO: test it
"""
import fitz  # this is pymupdf
import os

def split_pdf_into_images_v1(pdf_path):
    doc = fitz.open(pdf_path)
    for i in range(len(doc)):
        for img in doc.get_page_images(i):
            xref = img[0]
            base = "%d.png" % (i,)
            pix = fitz.Pixmap(doc, xref)
            if pix.n < 5:       # this is GRAY or RGB
                pix.writePNG(base)
            else:               # CMYK: convert to RGB first
                pix1 = fitz.Pixmap(fitz.csRGB, pix)
                pix1.writePNG(base)
                pix1 = None
            pix = None  # free Pixmap resources

def split_pdf_into_images_v2(pdf_path):
    doc = fitz.open(pdf_path)
    for i in range(len(doc)):
        for img in doc.get_page_images(i):
            xref = img[0]
            base = "%d.png" % (i,)
            pix = fitz.Pixmap(doc, xref)
            if pix.n < 5:       # this is GRAY or RGB
                pix.writePNG(base)
            else:               # CMYK: convert to RGB first
                pix1 = fitz.Pixmap(fitz.csRGB, pix)
                pix1.writePNG(base)
                pix1 = None
            pix = None  # free Pixmap resources

            # Save each page as an image
            image_path = os.path.join(os.path.dirname(pdf_path), f"page_{i}.png")
            pix.writePNG(image_path)
            pix = None  # free Pixmap resources

#pdf_path = "./data/articles/grade.5.五上第一单元“心爱之物”优秀作文.pdf"
pdf_path = "./data/pdf_sample.pdf"
split_pdf_into_images_v2(pdf_path)