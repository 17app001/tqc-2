import json,csv

# 開啟json
with open('read.json',encoding='utf-8') as f:
    datas=json.load(f)       
    
# 取出必要的key
datas=[[data['title'],data['showUnit'],data['startDate'],data['endDate']] 
 for data in datas]

# 另存csv
with open('write.csv','w',newline='',encoding='utf-8-sig') as f:
    writer=csv.writer(f)
    writer.writerows(datas)