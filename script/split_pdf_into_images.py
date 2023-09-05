import fitz  # this is pymupdf

def split_pdf_into_images(pdf_path):
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

pdf_path = "../kb/unstructured/domain.教培/math/6年级上册.pdf"
split_pdf_into_images(pdf_path)