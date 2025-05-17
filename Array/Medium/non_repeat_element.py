l=[1,2,3,2,4,3,5,6,4,3,4,5,4,5,4]
for i in l:
    if l.count(i)<=1:
        break
print("first non-repeat element :",i)