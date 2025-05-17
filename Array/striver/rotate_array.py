def rotate_array_with_given_size(n,k,s):
    k=k%n  #when k value greater than n then minimize the value using mod
    def reverse(start,end):
        while start<end:
            s[start],s[end]=s[end],s[start]
            start+=1
            end-=1
    
    #right Rotation
    reverse(0,n-1)  #reverse n element   [7, 6, 5, 4, 3, 2, 1]
    reverse(0,k-1)  #reverse k element   [5, 6, 7, 4, 3, 2, 1]
    reverse(k,n-1)  #reverse n-k element [5, 6, 7, 1, 2, 3, 4] 
    
    # Left Rotation
    # reverse(k,n-1)  #reverse n-k element  [1, 2, 3, 7, 6, 5, 4]
    # reverse(0,k-1)  #reverse k element    [3, 2, 1, 7, 6, 5, 4]
    # reverse(0,n-1)  #reverse n element  [4, 5, 6, 7, 1, 2, 3]
    return s


if __name__=="__main__":
    n=int(input("Enter how mny element you "))
    k=int(input("Enter how mny element you "))
    s=list(map(int,input("Enter element in space ").split()))
    print(rotate_array_with_given_size(n,k,s))