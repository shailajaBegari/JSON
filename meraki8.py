import json
list=[["neelam","programer","24","2400"],
["komal","trainer","24","20000"],
["anuradha","HR","25","40000"],
["Abhishek","manager","29","63000"]]
details=["name","designation","age","salary"]
emp=["emp1","emp2","emp3","emp4"]
d={}
e=0
for i in list:
    d1={}
    k=0
    for j in i:
        d1[details[k]]=j
        k=k+1
    d[emp[e]]=d1
    e=e+1
with open("emp.json","r+") as f:
    data=json.dump(d,f,indent=4)
    






