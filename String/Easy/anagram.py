#Check two string is anagram if both are sorted equals to each other
# s1="listen"
# s2="silent"
# s1="".join(sorted(s1))
# s2="".join(sorted(s2))
# if s1==s2:
#     print("Both are Anagram")
# else:
#     print("Not Anagram")

#Sort String
s="listen"
l=list(s)
n=len(l)
for i in range(n-1):
    for j in range(n-i-1):
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
print("".join(l))