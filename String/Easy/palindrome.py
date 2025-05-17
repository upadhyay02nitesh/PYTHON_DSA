def check_palin(l):
    s=[]
    for i in l:
        if i==i[::-1]:
            s.append(i)
    return s


n=3
l=[]
for i in range(n):
    l.append(input())
j=check_palin(l)
for i in j:
    print(i)

