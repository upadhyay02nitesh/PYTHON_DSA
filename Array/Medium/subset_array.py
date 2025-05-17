l=[11,1,13,21,3,7]
m=[11,3,7,1]
c=0
for i in m:
    if i in l:
        c+=1 
if(c==len(m)):
    print(m,"Is subset of", l)
else:
    print(m,"Is not subset of", l)
