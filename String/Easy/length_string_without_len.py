# s="Nitesh"
# l=0
# for i in s:
#     l+=1
# print(l)

#recursion

def str_len(s):
    if s=='':
        return 0
    else:
        return 1+str_len((s[1:]))
print(str_len("Nitesh"))

# 1+str_len("itesh")  =1+4+1=6
#     1+str_len("tesh")  =1+3+1
#         1+str_len("esh") =1+2+1
#             1+str_len("sh") =1+1+1
#                 1+str_len("h")=1+1
#                     1+" "           =1