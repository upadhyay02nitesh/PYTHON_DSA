l=[12,3,4,1,6,9]
sum=24
n=len(l)

for i in range(n):
   
    for j in range(i+1,n):
       
        for k in range(j+1,n):
            
            if l[i]+l[j]+l[k]==sum:
                print("Sum",sum,"find in the tripplet of",l[i],l[j],l[k])
          
            

