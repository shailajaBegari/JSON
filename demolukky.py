import json
d={"name":"laxmi","age":22,"nick":"lukky","friends":"swapna,shailu"}
with open("lukky.json","w") as f:
    json_string=json.dump(d,f,indent=2)
f.close()