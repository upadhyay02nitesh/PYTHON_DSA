def fact(n):
    if n==0:
        return 1
    f=1
    for i in range(1,n+1):
        f=f*i 
    return f


n=int(input("Enter the Number of the input to find factorial : "))
if __name__=="__main__":
    print(fact(n))