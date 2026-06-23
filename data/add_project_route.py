import json 
data = json.load(open('./data/data.json' , "r" ,encoding ='utf-8'))
def add(project):
    project['id'] = project['title'].replace(' ' , '_')
    data["projects"] = [project , *data["projects"]]
    with open('./data/data.json' , "w" ,encoding ='utf-8')as f:
        json.dump(data, f, indent=2)
