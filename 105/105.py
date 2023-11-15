# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 20:52:44 2023

@author: USER
"""


import sqlite3


conn=sqlite3.connect('read.db')
cursor=conn.cursor()

datas=list(cursor.execute('select * from Employee'))

for data in datas:
    print(data)
    
conn.close()