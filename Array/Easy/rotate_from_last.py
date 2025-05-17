def rotate_array(l,n):
    # return l[-1:]+l[:-1]
    s=l[-1]
    
    for i in range(n-1,0,-1):
        l[i]=l[i-1]
    l[0]=s
    return l
        


n=int(input("Enter the Number of the input : "))
l=list(map(int,input("Enter Element in one line with space ").split()))[:n]
if __name__=="__main__":
    print(rotate_array(l,n))