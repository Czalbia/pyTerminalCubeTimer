import json

with open('data.json', 'r+') as f:
    data = json.load(f)
    for  i in data['averages']:
        data['averages'][i]=0

    data['times']={}
    data['best']=0
    data['worst']=0
    data['count']=0
    f.seek(0)  
    json.dump(data, f, indent=4)
    f.truncate()