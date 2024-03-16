""" USE baidu OCR service to extract text from files """
from aip import AipOcr

""" 读取文件 """
def get_file_content(filePath):
    with open(filePath, "rb") as fp:
        return fp.read()

""" TODO: Fill in APPID AK SK """
""" GET info from https://console.bce.baidu.com/ai/#/ai/ocr/app/list """
""" 注意在不同场景下需使用不同的百度ocr服务 如公式与试卷识别 通用文字识别等"""

APP_ID = ''
API_KEY = ''
SECRET_KEY = ''
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

OCR_MODE = 0 # 0 for general purpose 1 for math formula

""" List files under the base_path """
import os
base_path = "../data/articles/grade.5.unit.1/"
file_paths = []
for file_name in os.listdir(base_path):
    if file_name.endswith(".DS_Store"):
        pass
    else:
        file_paths.append(os.path.join(base_path, file_name))
for file_name in file_paths:
    print(file_name)
print(len(file_paths))

for input_file_path in file_paths:
    output_file_path = input_file_path[:-4] + ".v1" + ".txt"
    print(input_file_path)
    print(output_file_path)
    image = get_file_content(input_file_path)

    if OCR_MODE == 0:
        # 调用通用文字识别（标准版）
        res_image = client.basicGeneral(image)
    elif OCR_MODE == 1:
        # 调用公式识别
        res_image = client.formula(image)
    else:
        print("NOT supported OCR_MODE:", OCR_MODE)
        exit(1)

    print(res_image)
    with open(output_file_path, 'w') as f:
        for result in res_image['words_result']:
            #print(result['words'])
            f.write(result['words'])
            f.write('\n')