# s="Nitesh"
# l=""
# for i in s:
#     l=i+l

# print(l)


#Reverse Word

# s="Nitesh Upadhyay Shahpur"
# s=s.split()
# l=""
# for i in range(len(s)-1,-1,-1):
#     if i>0:
#         l=l+s[i]+" "
#     else:
#         l=l+s[i]
    
# print(l)


s="Nitesh Upadhyay Shahpur"
s=s.split()
s=s[::-1]
l=" ".join(s)
print(l)


s="Nitesh Upadhyay Shahpur"
s=s.split()
l=""
n=len(s)
for i in range(n):
    s[i]=s[i][::-1]
    if i!=n-1:
        l=l+s[i]+" "
    else:
        l+=s[i]
print(l)