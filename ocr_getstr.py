import cv2
import os
import time
from aip import AipOcr

AppId = 'appid'
APIKey = 'apikey'
SecretKey = 'secretkey'
text = dict()
result = []
result_str = ''
path = 'workspace/1.png'    

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

def run(lang):
    global result_str
    result_str = ''
    client = AipOcr(AppId, APIKey, SecretKey)
    # image_input = cv2.imread(path,cv2.IMREAD_GRAYSCALE)
    img1 = get_file_content(path)

    options = {}
    options["language_type"] = lang

    time.sleep(1)
    text = client.basicGeneral(img1,options=options)
    # print(text)
    text = text["words_result"]
    for i in range(len(text)):
        if text[i]["words"] not in result:
            # result.append(text[i]["words"])
            str_ocr = text[i]["words"]
            result_str = result_str + str_ocr

    return result_str
