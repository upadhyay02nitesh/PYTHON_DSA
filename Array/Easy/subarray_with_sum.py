l=[1,4,20,3,10,5]
sum=33 

for i in range(len(l)):
    s=l[i]
    for j in range(i+1,len(l)):
        s=s+l[j]
        if s==sum:
            print("Sum Find Between",i,"and",j,"Position")


# i(0,6):
#     s=l[0]=1
#     j(i+1,6):
#         s=s+l[j]
#         if 5==33:
#             no 

#         if 25=33
#             no
#     i=2
#     s=l[2]=20
#         j(3,6):
#         if 23=33:
#             no 
#         if 33=33:
#             yes i,j =2,4

