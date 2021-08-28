 
import json
dict1 ={
    "emp1": {
        "name": "Lisa",
        "designation": "programmer",
        "age": "34",
        "salary": "54000"
    },
    "emp2": {
        "name": "Elis",
        "designation": "Trainee",
        "age": "24",
        "salary": "40000"
    },
} 
with open("myfile.json","w") as f:
    json_string=json.dump(dict1,f,indent=4)
f.close()
# print(type(json_string))





