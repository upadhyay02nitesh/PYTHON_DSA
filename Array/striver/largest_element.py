
n=4
for i in range(1,n+1):
    ord=64
    for j in range(n-i):
        print(" ",end="")
    for j in range(1,i+1):
        print(chr(ord+j),end="")
    for j in range(i-1,0,-1):
        print(chr(ord+j),end="")
    print()