import xml.etree.ElementTree as ET
import csv


tree=ET.parse('read.xml')
root=tree.getroot()

datas=[]
for row in root:  
    datas.append([row.find('sno').text,row.find('sna').text,row.find('tot').text])

with open('write.csv','w',newline='',encoding='utf-8-sig') as f:
    writer=csv.writer(f)
    writer.writerows(datas)