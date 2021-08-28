import json
with open("3.json","r") as f:
    data=json.load(f)
index=int(input("enter index  number:"))
Name=input("enter a name:")
id=input("enter id number:")
collage=input("enter collage name:")
for i in data[index]:
    if i=="name":
        data[index]["name"]=Name
    if i=="id":
        data[index]["id"]=id
    if i=="collage":
        data[index]["collage"]=collage
print(data)