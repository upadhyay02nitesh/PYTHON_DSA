s="the quick brown fox jumps over the lazy dog"
s=s.split()
print(s)
l=[]
for i in s:
    if i not in l:
        l.append(i)
c=0
for i in l:
    c=0
    for j in s:
        if i==j:
            c+=1
    print(i,c)
