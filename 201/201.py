# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 21:21:24 2023

@author: USER
"""

import requests,re


url='https://www.codejudger.com/target/5201.html'
resp=requests.get(url)

if resp.status_code==200:
    html_text=resp.text
    key=input('請輸入欲搜尋的字串 : ')    
    # 使用正則式重複查找關鍵文字
    size=len(re.findall(key,html_text))    
    if size>0:    
        print(f'{key} 搜尋成功')    
        print(f'{key} 出現 {size} 次')    
    else:
        print(f'{key} 搜尋失敗')    
        print(f'{key} 出現 0 次')    
else:
    print("網頁下載失敗")