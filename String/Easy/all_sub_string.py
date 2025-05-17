s="abcd"
n=len(s)
for i in range(n):
    for j in range(i+1,n+1):
        print(s[i:j])
    


# i=0 
#     j=(i+1,n+1)=(1,5)
#     print(s[0:1])=a
#     print(s[0:2])=ab
#     print(s[0:3])=abc
#     print(s[0:4])=abcd

# i=1
#     j=(i+1,n+1)=(2,5)
#     print(s[1:2])=b
#     print(s[1:3])=bc
#     print(s[1:4])=bcd
# i=2 
#     j=(i+1,n+1)=(3,5)
#     print(s[2:3])=c
#     print(s[2:4])=cd
# i=3 
#     j=(i+1,n+1)=(4,5)
#     print(s[3:4])=d


   