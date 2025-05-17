def bubble_sort(l):
    n=len(l)
    for i in range(n-1):
        for j in range(n-i-1):
            if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
    return l 
l=[3,5,6,2,1]
print(bubble_sort(l))

# Lets understand working flow 

# for i(4):
#         for j(4-0-1):
#             if l[0]>l[1]:
#                 l[0],l[1]=l[1],l[0]

# 3>5 =no 
# 5>6 =no 
# 6>2=yes
# 6,2=2,6
# 6>1=yes
# 6,1=1,6

# after first iteration  3 5 2 1 6

# after each iteration we found max element in last
