m=[1,2,3,2,5,5,4,3,2,4,5,2]
s=[]
l=[]

#remove duplicate and store occurrence value
for i in m:
    if i not in s:
        l.append(m.count(i))

#find max occurrence
max=0
for i in l:
    if i>max:
        max=i 


#match max occurrence value with actual number
for i in m:
    if m.count(i)==max:
        break 
print(i,"Occurres max time :",max)
