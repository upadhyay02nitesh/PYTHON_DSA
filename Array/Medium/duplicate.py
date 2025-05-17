l=[1,2,3,4,3,2,1,2,3]
g=[]
for i in l:
    if i not in g:
        g.append(i)
for i in g:
    if l.count(i)>1:
        print(i,end=" ")