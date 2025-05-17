def rotation(s,t):

    size1=len(s)
    size2=len(t)
    if size1!=size2 or s==t:
        return False

    temp=s+s  #(abcd+abcd=abcdabcd)

    if t in temp:
        return True


if __name__=="__main__":
    s=input("Enter the String : ")
    t=input("Enter the String : ")
    print(rotation(s,t))