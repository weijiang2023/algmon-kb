"""
The program is a Python script that uses the PyPDF2 library to split a PDF file into two separate PDF files.
"""
import PyPDF2

def split_pdf(input_path, output_path1, output_path2, split_page):
    # 打开PDF文件
    with open(input_path, 'rb') as file:
        pdf = PyPDF2.PdfReader(file)
        
        # 创建两个新的PDF写入对象
        output1 = PyPDF2.PdfWriter()
        output2 = PyPDF2.PdfWriter()
        
        # 分割PDF
        for page_num in range(len(pdf.pages)):
            page = pdf.pages[page_num]
            
            if page_num < split_page:
                # 将页面添加到第一个输出对象
                output1.add_page(page)
            else:
                # 将页面添加到第二个输出对象
                output2.add_page(page)
        
        # 将切割后的PDF保存到文件
        with open(output_path1, 'wb') as file1:
            output1.write(file1)
        
        with open(output_path2, 'wb') as file2:
            output2.write(file2)

# 指定输入PDF文件路径
input_pdf = ''

# 指定输出的两个PDF文件路径
output_pdf1 = ''
output_pdf2 = ''

# 指定切割的页面数
split_page_number = 5

# 调用函数进行PDF切割
split_pdf(input_pdf, output_pdf1, output_pdf2, split_page_number)

print("PDF切割完成！")
