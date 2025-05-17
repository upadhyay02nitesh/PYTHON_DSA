l=[1,2,3,4]
m=[1,2,3]
n=[1,2,4]

intersect=[]
intersect1=[]
for i in l:
    if i in m:
        intersect.append(i)
for i in intersect:
    if i in n:
        intersect1.append(i)
print(intersect1)



