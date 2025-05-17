l=[0,2,1,2,1,3,4,2,10,10,10,10,10]
ele=l[0]
s=l.count(l[0])
for i in range(1,len(l)):
    if l.count(l[i])>s:
        s=l.count(l[i])
        ele=l[i]
print(ele,"Occurres max :",s,"times")
