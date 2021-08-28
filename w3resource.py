# import json
# json_obj = '{ "Name":"David", "Class":"I", "Age":6 }'
# python=json.loads(json_obj)
# print(json_obj["Name"])
#################
# import json
# python_obj = {
#   "name": "David",
#   "class":"I",
#   "age": 6  
# }
# with open("namelist.json","w") as f:
#     json_string=json.dump(python_obj,f,indent=4)
# f.close()
########################

import json
dic={'4': 5, '6': 7, '1': 3, '2': 4}
print(json.dumps(dic,sort_keys=True,indent=4))
##############################
# import json
# obj_dict = '{"name": "David", "age": 6, "class": "I"}'
# obj_list = '["Red", "Green", "Black"]'
# obj_string = '"Python Json"'
# obj_int = '1234'
# print(json.loads(obj_dict))
# print(json.loads(obj_string))
######################

# import json
# d={"name":"shailu","husband":"nani"}
# with open("example.json","r") as f:
#     json_string=json.load(f)
# # f.close()
# print(json_string)

##############
import json
dict1={'complex':2+3j}
with open("1.json","w") as f:
    json.dump(dict1,f ,indent=2)


#############################
# import json
# python_obj = '{"a":  1, "a":  2, "a":  3, "a": 4, "b": 1, "b": 2}'
# python_string=json.loads(python_obj)
# print(python_string)
