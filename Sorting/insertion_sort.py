
def insertion_sort(l):
    for i in range(1,len(l)):
        temp=l[i]
        j=i-1 
        while j>=0 and temp<l[j]:
           l[j+1]=l[j]
           j=j-1
        l[j+1]=temp
    return l
l=[5,4,3,2,1]
print(insertion_sort(l))

# lets understand through example 
# l=5,4,3,2,1
# for i in range(1,len(l)):
#     here we assign temp=l[i]=4 
#     and j=i-1=0 
#     while j>=0 yes and temp<l[j] means 4<5:
#             THEN l[j+1]=l[j]  means l[1]=l[0]=5
#             j=j-1 =-1

#     again check while loop j>=0 no its -1 
#     then we assign l[j+1]=l[-1+1]=l[0]=temp means l[0]=4
#     Now List bacome 4,5,3,1,2


#     again i become 2 and j=i-1=1 and temp=l[i]=l[2]=3
#         while j>=0 yes j=1 and temp<l[j] means 3<5 yes:
#                 l[j+1]=l[j] means l[2]=5
#                 j=j-1 =0 
#         while j>=0 yes j=0 and temp<l[j] means 3<4 yes:
#                 l[j+1]=l[j] means l[1]=4 
#                 j=j-1 =0-1=-1
#         then while j>=0 no j become -1 

#         THEN l[j+1]=temp means l[-1+1]=l[0]=3 
        
#         Now List bacome 3,4,5,1,2
    
# We can also traverse 2 and 1 untill we will found 1,2,3,4,5
        


