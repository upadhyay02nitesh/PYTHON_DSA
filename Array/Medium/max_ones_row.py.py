m=[[0,1,1],
   [1,1,1],
    [1,0,1]]
max=0
ele=0
for i in range(len(m)):
    c=0
    for j in range(len(m[i])):
        if m[i][j]==1:
            c+=1
            if c>max:
                max=c 
                ele=i
print(max,"find in :",ele,"row")
        
