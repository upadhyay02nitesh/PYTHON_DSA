def merge_sort(l):
    if len(l)>1:
        mid=len(l)//2 
        left=l[:mid]
        right=l[mid:]

        merge_sort(left)
        merge_sort(right)

        i=j=k=0 
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                l[k]=left[i]
                i+=1
                k+=1 
            else:
                l[k]=right[j]
                j+=1 
                k+=1
        
        while i<len(left):
            l[k]=left[i]
            i+=1 
            k+=1

        while j<len(right):
            l[k]=right[j]
            j+=1 
            k+=1
    return l 
l=[5,4,3,2,1]
print(merge_sort(l))


# Lets Understand working flow --:

# l=[5,4,3,2,1]
# if len(l)>1 yes len(l)=5 

#     now mid=5//2=2
#     left=l[:mid]=l[0:2]=[5,4]
#     right=l[mid:]=l[2:]=[3,2,1]

#     merge_sort(left)
#     merge_sort(right)


# merge_sort(left)=merge_sort([5,4])
# if len(l)>1 yes its 2 :
#     now mid=2//2 =1 
#     left=l[0:1]=[5]
#     right=l[1:]=[4]
#     merge_sort(left)
#     merge_sort(right)
# now len(left)>1 no False
#     then its 5
# and len(right)>1 no False:
#     then its 4 
# now both are compare 5<4:
#     no 
#     then l[k]=[4,5]
