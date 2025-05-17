s="aeghldhlfhlnslueigytrqoiumnbgfhzeydfruiluqrqdaqajga"
s="".join(sorted(s))
p=""
for i in s:
    if i not in p:
        p+=i 
# for i in p:
#     print(i,"Occurrence :",s.count(i))

for i in p:
    k=0
    for j in s:
        if i==j:
            k+=1
    print(i,"Occurrence :",k)