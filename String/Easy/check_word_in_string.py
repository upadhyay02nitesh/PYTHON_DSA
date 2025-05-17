
def present(s,k):
    s=s.split()
    if k in s:
        return True
    return False

s="this is a bus"
k="bus"
p=present(s,k)
if p==True:
    print(k,"is present in ",s)
else:
    print(k," is not present in ",s)