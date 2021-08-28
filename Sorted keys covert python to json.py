import json
d={
    '4': 5, 
    '6': 7, 
    '1': 3, 
    '2': 4}
d1={}
for x in sorted(d.keys()):
     d1[x]=d[x]
     json_string=json.dumps(d1,indent=4)
print(json_string)
print(type(json_string))

########################################

print(json.dumps(d,sort_keys=True,indent=4))



# output:::
# {
#     "1": 3,
#     "2": 4,
#     "4": 5,
#     "6": 7
# }