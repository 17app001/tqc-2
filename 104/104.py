import json


datas={
'people' :
[{  
    'id': '1',
    'name': 'Peter',
    'country': 'Taiwan'
},
{  
    'id': '2',
    'name': 'Jack',
    'country': 'USA'
},
{  
    'id': '3',
    'name': 'Cindy',
    'country': 'Japan'
}]
}
    
with open('write.json','w') as f:
    json.dump(datas,f)