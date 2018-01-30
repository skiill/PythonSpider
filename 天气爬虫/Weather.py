# Author xsj

import urllib.request
import json

def get_dic(url):
    page = urllib.request.urlopen(url)
    html = page.read().decode('utf-8')
    page.close()
    dic=json.loads(html)
    return dic

dic = get_dic("http://www.weather.com.cn/data/cityinfo/101010100.html")

print(dic['weatherinfo']['city'])
print(dic['weatherinfo']['ptime'])
print(dic['weatherinfo']['temp1'])
print(dic['weatherinfo']['temp2'])
print(dic['weatherinfo']['weather'])