# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 20:23:41 2023

@author: USER
"""


import json,yaml

# 開啟json
with open('read.json',encoding='utf-8') as f:
    datas=json.load(f)    
    
# 轉存yaml
with open('write.yaml','w',encoding='utf-8') as f:
    yaml.dump(datas,f,allow_unicode=True)


