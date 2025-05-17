l=[1,2,3,4,5]
last_elemnt=l[len(l)-1]
for i in range(len(l)-1,0,-1):
    l[i]=l[i-1]
l[0]=last_elemnt
print(l)
    

# last_ele=l[len(l)-1]
# i(4,0,-1)
#     a[i]=a[i-1]
#     a[4]=4
#     a[3]=3
#     a[2]=2
#     a[1]=1
# a[0]=last_ele
# a[0]=5
