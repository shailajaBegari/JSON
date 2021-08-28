import json 
d={"name": "David",
     "class":"I",
     "age": 6 }
json_string=json.dumps(d,indent=4)
print(json_string)