
def remove_duplicate(n,s):
    if not s:
        return 0
      # k
    # 0 0 1 1 2 2
        # k
    # 0 1 1 1 2 2 
          # k
    # 0 1 2 1 2 2

    k=1
    
    for i in range(1,n):
        if s[i]!=s[k-1]:
            s[k]=s[i]
            k+=1
    return k



if __name__=="__main__":
    n=int(input("Enter how mny element you "))
    s=list(map(int,input("Enter element in space ").split()))
    print(remove_duplicate(n,s))