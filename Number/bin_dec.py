a=10
temp=a 
s=0
power=0
while temp>0:
    r=temp%10 
    s+=r*(2**power)
    # if r=0 then 0*(2**0)=0*1=1
    # if r=1 then 1*(2**0)=1
    temp//=10 
    power+=1
print(s)
        
