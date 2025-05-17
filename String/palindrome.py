def palindrome(s):
    s1=""
    for i in s:
        s1=i+s1 
    if s==s1:
        return True
    return False


  
if __name__=="__main__":
    s=input("Enter the String : ")
    print(palindrome(s))