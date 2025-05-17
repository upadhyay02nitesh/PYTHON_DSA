def selection_sort(l):
    n=len(l)
    for i in range(n-1):
        for j in range(i+1,n):
            if l[i]>l[j]:
                l[i],l[j]=l[j],l[i]
    return l 
l=[5,4,3,2,1]
print(selection_sort(l))

# Lets understand working flow 

# for i(4):
#         for j(0+1,4):
#             if l[0]>l[1]:
#                 l[0],l[1]=l[1],l[0]

# if 5>4 yes 4,5 [4,5,3,2,1]
# 4>3 yes 3,4    [3,5,4,2,1]
# 3>2 yes 2,3    [2,5,4,3,1]
# 2>1 yes 1,2    [1,5,4,3,2]

# after each iteration we found min element in first