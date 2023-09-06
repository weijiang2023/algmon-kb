"""
USE baidu OCR service to extract questions and output them to files in text
"""
from aip import AipOcr

""" TODO: Fill in APPID AK SK """
""" GET info from https://console.bce.baidu.com/ai/#/ai/ocr/app/list """
APP_ID = ''
API_KEY = ''
SECRET_KEY = ''
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

""" Load the csv files """
import csv
file_paths = []
for i in range(0,118):
    #print(str(i) + ".png")
    file_paths.append(str(i) + ".png")

""" 读取文件 """
def get_file_content(filePath):
    with open(filePath, "rb") as fp:
        return fp.read()

base_path = "../kb/unstructured/domain.教培/math/grade.5.上/core/"

for input_file_path in file_paths:
    print(input_file_path)
    output_file_path = base_path + input_file_path.split(".")[0] + ".txt"
    #print(output_file_path)
    image = get_file_content(base_path + input_file_path)
    # 调用通用文字识别（标准版）
    res_image = client.basicGeneral(image)
    
    #print(res_image['words_result'])
    with open(output_file_path, 'w') as f:
        for result in res_image['words_result']:
            #print(result['words'])
            f.write(result['words'])
            f.write('\n')