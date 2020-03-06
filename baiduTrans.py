#百度通用翻译API,不包含词典、tts语音合成等资源，如有相关需求请联系translate_api@baidu.com
# coding=utf-8

import http.client
import hashlib
import urllib
import random
import json

appid = 'appid'  # 填写你的appid
secretKey = 'secreckey'  # 填写你的密钥

httpClient = None
myurl = '/api/trans/vip/translate'

def trans_get(from_l,to_l,q_t):
    global myurl,httpClient
    fromLang = from_l   #原文语种
    toLang = to_l   #译文语种
    salt = random.randint(32768, 65536)
    q= q_t
    sign = appid + q + str(salt) + secretKey
    sign = hashlib.md5(sign.encode()).hexdigest()
    myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
    salt) + '&sign=' + sign

    try:
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)

        # response是HTTPResponse对象
        response = httpClient.getresponse()
        result_all = response.read().decode("utf-8")
        result = json.loads(result_all)

        return result['trans_result'][0]['dst']

    except Exception as e:
        return '[ERROR]发生错误，请稍后重试'

    finally:
        if httpClient:
            httpClient.close()