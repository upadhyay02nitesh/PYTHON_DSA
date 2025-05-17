s="ewuidjleoinkshoid"
v=['a','e','i','o','u','A','E','I','O','U']
c=""
for i in s:
    if i.isalpha():
        if i not in v:
            c+=i 
print(c)



    