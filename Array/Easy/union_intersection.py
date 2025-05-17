l1=[1,2,3,4,5,6]
l2=[0,3,4,5,6,7]

# for i in l2:
#     if i not in l1:
#         l1.append(i)
# l1.sort()
# print("Union ->",l1)


# intersect=[]
# for i in l1:
#     if i in l2:
#         intersect.append(i)
# print("Intersection ->",intersect)

diff=[]
for i in l2:
    if i not in l1:
        diff.append(i)
print(diff)


# l1=set(l1)
# l2=set(l2)
# print(list(l1.union(l2)))
# print(list(l1.intersection(l2)))
# print(list(l1.difference(l2)))
    
    