# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 21:48:49 2023

@author: USER
"""


from bs4 import BeautifulSoup
import pandas as pd

with open('read.html',encoding='utf-8-sig') as f:
    html_text=f.read()
    
soup=BeautifulSoup(html_text,'lxml')
trs=soup.find('table',class_="DataTable2").find_all('tr')

datas=[]
for tr in trs:
    data=[]
    for th in tr.find_all('th'):
        #print(th.text.strip(),end='\t')
        data.append(th.text.strip())
    for td in tr.find_all('td'):
        #print(td.text.strip(),end='\t')
        data.append(td.text.strip())
    #print()
    datas.append(data)
    

df=pd.DataFrame(datas[1:],columns=datas[0])

df.set_index('日 期').to_csv('write.csv',encoding='utf-8-sig')
