def linear_search(l,s):
    for i in l:
        if i==s:
            return True
    return False

l=[1,3,5,4,2]
s=2
f=linear_search(l,s)
if s==True:
    print(s,"Find in the list")
else:
    print(s,"is not in the list")