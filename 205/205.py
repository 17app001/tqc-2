# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 20:12:56 2023

@author: USER
"""

import requests,json


url='https://www.codejudger.com/target/5205.json'

resp=requests.get(url)

datas=json.loads(resp.text)
# 取得內容實際大小 
print(f'Content-Length: {len(resp.content)}\n')
print('新北市PM2.5相關資料：')
for data in datas:
    if data['County']=='新北市':
        print(f"{data['SiteName']}：")
        print(f"\tAQI：{data['AQI']}")
        print(f"\tPM2.5：{data['PM2.5']}")
        print(f"\tPM10：{data['PM10']}")
        print(f"\t資料更新時間：{data['PublishTime']}")