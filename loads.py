# import json
# dic='''{
#     "name":"shailu",
#     "Age":"21",
#     "qualification":"degree"
#     }'''
# json_string=json.loads(dic)
# print(type(json_string))
# print(json_string["name"])




import json
x = '{ "name":"John", "age":true, "city":"New York"}'
y = json.loads(x)
# the result is a Python dictionary:
print(y)
print(type(y))