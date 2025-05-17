def duplicate(s):
    s1=""
    for i in s:
        c=s.count(i)
        if c>1 and i not in s1:
            s1=s1+i
    return s1


  
if __name__=="__main__":
    s=input("Enter the String : ")
    print(duplicate(s))