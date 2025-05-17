def quick_sort(l):
    if len(l)<=1:
        return l
    else:
        pivot=l.pop()
        left=[]
        right=[]
        for i in l:
            if i>pivot:
                right.append(i)
            else:
                left.append(i)
        return quick_sort(left)+[pivot]+quick_sort(right)
l=[1,6,8,11,12,10]
print(quick_sort(l))        


# Lets stand working flow

# l=[1,6,8,11,12,10]

# if len(l)<=1:
#     return l  means len(l)=6<=1 return l

# else:
#     now take last element as pivot 
#     pivot=l.pop()
#     we delete last element and store in pivot 
#     now take two list left and right 
#     and apply for loop on popped list 
#     left=[1,6,8]
#     right=[11,12]
#     return quick_sort(left)+[pivot]+quick_sort(right)
#             quick_sort([1,6,8])+[10]+quick_sort([11,12])
    

# lets understand left quick_sort
# left =[1,6,8]
# if len(l)<=1 yes l=3 return l 
# pivot=l.pop()=8 
# apply loop left=[1,6]
# right=[8]
# now quick_sort(left)+[pivot]+quick_sort(right)
#     quick_sort([1,6])+[8]+quick_sort([])
#                             now right empty it return empty list 


# we follow these Recursion untill list become [1,6,8,10,11,12]