l=[3,3,4,2,4,4,2,4,4]
n=len(l)
s=len(l)//2
max=0
ele=0
for i in l:
    if l.count(i)>max:
        max=l.count(i)
        ele=i 
if max>s:
    print("Majority element ",ele,"-> repeat",max,"- times greater  than the size of half array",s)
else:
    print("No majority element ")