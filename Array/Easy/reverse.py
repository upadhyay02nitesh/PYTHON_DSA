def reverse_arr(l):
    s=[]
    for i in l:
        s.insert(0,i)
    return s
  
l=[1,2,3,4,5]
m=reverse_arr(l)
print(m)


def reverse_arr(l):
    s=[]
    for i in range(len(l)-1,-1,-1):
        s.append(l[i])
    return s
  
l=[1,2,3,4,5]
m=reverse_arr(l)
print(m)

def reverse_arr(l):
    l=l[::-1]
    return l
  
l=[1,2,3,4,5]
m=reverse_arr(l)
print(m)

def reverse_arr(l):
    l.reverse()
    return l
  
l=[1,2,3,4,5]
m=reverse_arr(l)
print(m)

s=[1,2,3,4]
n=len(s)
l=[0]*n

for i in range(n):
    l[i]=s[n-i-1]
print(l)