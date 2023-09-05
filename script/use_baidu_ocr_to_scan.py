from aip import AipOcr

""" 你的 APPID AK SK """
""" GET them from https://console.bce.baidu.com/ai/#/ai/ocr/app/list """
APP_ID = ''
API_KEY = ''
SECRET_KEY = ''

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

""" 读取文件 """
def get_file_content(filePath):
    with open(filePath, "rb") as fp:
        return fp.read()

image = get_file_content('./data/ocr_image_sample.png')
url = "https://www.x.com/sample.jpg"
pdf_file = get_file_content('./data/pdf_sample.pdf')

# 调用通用文字识别（标准版）
res_image = client.basicGeneral(image)
#res_url = client.basicGeneralUrl(url)
#res_pdf = client.basicGeneralPdf(pdf_file)
print(res_image)
#print(res_url)
#print(res_pdf)

# 如果有可选参数
options = {}
options["language_type"] = "CHN_ENG"
options["detect_direction"] = "true"
options["detect_language"] = "true"
options["probability"] = "true"
res_image = client.basicGeneral(image, options)
res_url = client.basicGeneralUrl(url, options)
res_pdf = client.basicGeneralPdf(pdf_file, options)
print(res_image)
#print(res_url)
#print(res_pdf)