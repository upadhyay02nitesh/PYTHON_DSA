s="ahbgdc"
k="abch"
n=len(k)
c=0
for i in k:
    for j in s:
        if i==j:
            c+=1
if n==c:
    print(k,"is subsequence of",s)
else:
    print(k,"is not subsequence of",s)