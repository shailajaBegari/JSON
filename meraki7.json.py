# import json
# file_name="meraki7.json"
# dict={}
# with open (file_name) as file:
#     for line in file:
#         key,value=line.strip().split(None,1)
#         dict[key]=value.strip()
        # python_string=json.dumps(dict,indent=4)
# print(python_string)
# f.close()


import json
text='''Name  Abhishek
    Designation CEO of navgurukul
    Gender male
    Age 29'''
a=text.split()
# print(a)
d={}
i=0
j=1
while i<len(a):
    if i%2==0:
        b=a[i]
        d[b]=a[j]
    j=j+1
    i=i+1
# print(d)
with open("saral7.json","w") as f:
    json_string=json.dump(d,f,indent=4)



