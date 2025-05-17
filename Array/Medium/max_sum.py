l=[8,3,1,2]
n=len(l)
max=0

for i in range(n):
    if i>0:
        l=l[1:]+l[:1]
    product=l[i]*0
    for j in range(1,n):
        product+=l[j]*j
    # print(product)
    if product>max:
        max=product
    
print("Maximum Sum Is :",max)

# Explanation--:
# i=0           8,3,1,2          8*0+3*1+1*2+2*3=11
# i=1           3,1,2,8          3*0+1*1+2*2+8*3=29
# i=2           1,2,8,3          1*0+1*2+8*2+3*3=27
# i=3           2,8,3,1          1*0+8*1+3*2+1*3=17

# max=29


