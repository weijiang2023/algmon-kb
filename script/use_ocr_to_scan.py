tech_provider = "pytesseract" # pytesseract, baidu, paddleocr
if tech_provider == "pytesseract":
    import pytesseract
    from pdf2image import convert_from_path
    print("mark 0")
    pdf_file = './data/pdf_sample.pdf'
    images = convert_from_path(pdf_file)
    ocr_text = ''
    print("mark 1")
    for image in images:
        ocr_text += pytesseract.image_to_string(image, lang='chi_sim')
        with open('ocr_output.txt', 'w') as output_file:
            output_file.write(ocr_text)
            ocr_output = 'ocr_output.txt'
elif tech_provider == "baidu":
    pass
elif tech_provider == "paddleocr":
    # TODO:
    pass