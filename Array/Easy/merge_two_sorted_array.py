
def merge_sorted_array(l,s,n,m):
    i,j=0,0
    k=n-1

    while (i<=k and j<m):
        if l[i]<s[j]:
            i+=1
        else:
            temp=s[j]
            s[j]=l[k]
            l[k]=temp
            j+=1
            k-=1
    l.sort()
    s.sort()
    


n=int(input("Enter the Number of the input : "))
m=int(input("Enter the Number of the input : "))
l=list(map(int,input("Enter Element in one line with space ").split()))[:n]
s=list(map(int,input("Enter Element in one line with space ").split()))[:n]
if __name__=="__main__":
    merge_sorted_array(l,s,n,m)
    print(l,end=" ")
    print(s)