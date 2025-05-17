def move_zero(n,s):
    # 1 0 1 0 2 4
    start=0
    i=0
    while i<n:
        if s[i]==0:
            s[start],s[i]=s[i],s[start]
            start+=1
        i+=1

    return s


if __name__=="__main__":
    n=int(input("Enter how mny element you "))
    s=list(map(int,input("Enter element in space ").split()))
    print(move_zero(n,s))