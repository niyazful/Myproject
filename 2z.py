import json

mayfile = "task_2.json"
with open(mayfile,encoding="utf-8") as read_file:
    data = json.load(read_file)
    data.sort(key=lambda user: user["shop"])
    print (data)
