def move_element(l,n):
    c0,c1,c2=0,0,0
    for i in l:
        if i==0:
            c0+=1
        elif i==1:
            c1+=1
        else:
            c2+=1
    i=0
    while(c0>0):
        l[i]=0 
        i+=1
        c0-=1
    while(c1>0):
        l[i]=1
        i+=1
        c1-=1
    while(c2>0):
        l[i]=2
        i+=1
        c2-=1
    return l



n=int(input("Enter the Number of the input : "))
l=list(map(int,input("Enter Element in one line with space ").split()))[:n]
if __name__=="__main__":
    print(move_element(l,n))