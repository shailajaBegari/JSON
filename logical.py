
import json
i=0
d={}
while i<10:
    name=input("enter name:")
    value=int(input("enter numbers:"))
    d[name]=value
    i=i+1
with open("list.json","w") as f:
    json_string=json.dump(d,f,indent=4)
f.close()