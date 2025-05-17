s="geeksforgeeks"
chars=[1,5,7,9]
for i in range(len(s)):
    if i in chars:
        print("*",end="")
    else:
        print(s[i],end="")