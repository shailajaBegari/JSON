f=open("1.text","w")
sum=0
i=0
while i<=5:
    user=int(input("enter number of days spending money:"))
    f.write(str(user))
    f.write("\n")
    sum=sum+user
    i=i+1
f.write(str(("total sum",sum)))
