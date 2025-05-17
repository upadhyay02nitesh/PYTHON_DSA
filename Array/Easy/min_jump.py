def min_jump(l,k):
    maxr=l[0]
    step=l[0]
    if n==1:
        return 0
    elif l[0]==0:
        return -1
    else:
        des=0
        pos=0
        jump=0
        # 1 3 5 8 9 2 6 7 8
        for i in range(0,n-1): # 0 1 2
            des=max(des,l[i]+i) # 1 4 6 9
            if pos==i: # 0y 1y 4 y
                pos=des # 1 4 9
                
                jump=jump+1 # 1 2 3
        return jump


n=int(input("Enter the Number of the input : "))

l=list(map(int,input("Enter Element in one line with space ").split()))[:n]
if __name__=="__main__":
    print(min_jump(l,n))