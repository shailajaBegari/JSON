# i=1
# k=15
# while i<=5:
#     m=k
#     j=1
#     l=4
#     while j<=i:
#         print(m,end=" ")
#         m=m-l
#         l=l-1
#         j=j+1
#     print()
#     i=i+1
#     k=k-1


# surname
user=input("enter sentence::")
b=user.split()
i=0
s=""
while i<len(b):
    if b[i]==b[0]:
        s=s+b[i][0] 
    else:
        s=s+"."+b[i]
    i=i+1
print(s)


