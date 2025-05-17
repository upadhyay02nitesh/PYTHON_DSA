# def rev_string(s):

#     # s=s[::-1]
#     # return s
    
#     s1=""
#     for i in s:
#         s1=i+s1
#     return s1

        

# if __name__=="__main__":
#     s=input("Enter the String : ")
#     print(rev_string(s))

def rev_string(s):

    # left=0
    # right=len(s)-1
    # while (left<right):
    #     s[left],s[right]=s[right],s[left]
    #     left+=1
    #     right-=1

    # return s
    s1=[]
    for i in range(len(s)-1,-1,-1):
        s1.append(s[i])

    return s1
  
if __name__=="__main__":
    n=int(input("Enter how many character : "))

    # s = list(input("Enter characters separated by spaces: ").split()[:n])
    s=['n','i','t','e','s','h']
    print(rev_string(s))