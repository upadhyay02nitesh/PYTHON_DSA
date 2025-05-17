
def common_long_prefix(s):
    if not s:
        return ""
    s.sort()
    # print(s)
    first=s[0]
    last=s[-1]
    ans=""
    # print(min(len(first),len(last)))
    for i in range(min(len(first),len(last))):
        
        if first[i]!=last[i]:
            return ans
        ans+=first[i]


    return ans
  
if __name__=="__main__":
    n=int(input("Enter how many character : "))

    s = list(input("Enter characters separated by spaces: ").split()[:n])
    print(common_long_prefix(s))