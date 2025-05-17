s="restart"
k=s[0]
n=len(s)
for i in range(n):
    if i>0:
        if s[i]==k:
            print("$",end="")
        else:
            print(s[i],end="")
    else:
        print(s[i],end="")
