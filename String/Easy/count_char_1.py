# s="aabbccc"
# c=""
# p=""
# for i in s:
#     if i not in c:
#         c+=i 
# for i in c:
#     d=s.count(i)
#     p+=i+str(d)
# print(p)


s="a2b3c4"
str=""
for i in s:
    if i.isdigit():
        str+=p*int(i) 
    else:
        p=i

print(str)

