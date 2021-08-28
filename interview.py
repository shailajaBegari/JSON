# import json
# list1=[]
# while True:
#     dict={}
#     username=input("enter user name:")
#     password=input("enter passaword:")
#     dict["username"]=username
#     dict["password"]=password
#     list1.append(dict)
#     print(list1)
#     with open("2.json","w") as f:
#         json_string=json.dump(list1,f,indent=4)
        



#####################################

###multable by table

num=int(input("enter  a num:"))
i=1
while i<=10:
    j=1
    while j<=num:
        # print(str(j)+"*"+str(i)+"="+str(j*i)+" ",end="")
        print(j*i,end="  ")
        j+=1
    print()
    i+=1

