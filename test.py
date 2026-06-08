import json
with open("data.json", "r") as file:
    data = json.load(file)
n = len(data['skills'])
for i in range(n):
    data['skills'][i] = {"name": data['skills'][i], "logo": ""}
with open("data.json", "w") as file:
    json.dump(data, file, indent=4)