s="this is school canteens"
s=s.split()
max=0
ele=""
for i in s:
    l=0
    for j in i:
        l+=1
    if l>max:
        max=l 
        ele=i 
print(i,max)
