# -*- coding: utf-8 -*-
# @Time    : 2023/4/7 2:31
# @Author  : Narain
# @Site    : 
# @PROJECT_NAME  : PythonLerning
# @File    : EasyDemo.py
import requests

# 组装请求
# url = "https://apis.tianapi.com/tianqi/index?key=d55beb94afdb93bd4d19e441ed975d19&city=101020100&type=1"
url = "https://apis.tianqi.com/tianqi/index"
param = {"key": "d55beb94afdb93bd4d19e441ed975d19", "city": "上海"}
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 "
                  "Safari/537.36"}
# 发送请求 获取响应
rep = requests.get(url=url, headers=headers, params=param)
# 解析响应

print(rep.text)
