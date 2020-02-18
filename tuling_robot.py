#coding=utf-8
import json
import requests

from wxpy import *

import config

tuling = Tuling(api_key=config.tuling_api_key)


def auto_reply(msg):
    return tuling.do_reply(msg)

if __name__ == '__main__':
    apikey = '7c8cdb56b0dc4450a8deef30a496bd4c'
    api_url = 'http://www.tuling123.com/openapi/api'
    data = {'key': apikey, 'info': 'Hello'}
    req = requests.post(api_url, data=data).text
    replys = json.loads(req)['text']
    print(replys)