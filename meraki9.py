import json
d={
    "shopping_list":
        { 
            "chaco":"15",
            "Biscuits":"50",
            "Diary_milk":"30",
            "ice_cream":"20",
        } 
}
item=input("enter item name:")
user=int(input("how many items do you want:"))
for i in d:
        if item in d[i]:
            d[i][item]=user
        else:
            d[i][item]=user
with open("shopping.json","w") as f:
    json.dump(d,f,indent=4)

###################################################

# import json
# shopping={"shopping_list":{"chaco":"15","Biscuits":"50","Diary_milk":"30","ice_cream":"20",}}
# item=input("enter the item:")
# no=int(input("how many item:"))
# c=shopping["shopping_list"][item]
# rem=int(c)-no
# shopping["shopping_list"][item]=rem
# b=json.dumps(shopping,indent=4)
# print(b)


