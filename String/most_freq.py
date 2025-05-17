def most_freq(s):
    max=s.count(s[0])
    s1={}
    for i in s:
        c=s.count(i)
        if c>max:
            max=c
            s1[i]=max
    return s1
     
    # check all occurrence
    # for i in s:
    #     c=s.count(i)
    #     if i not  in s1:
    #         s1[i]=c
        
    # return s1


  
if __name__=="__main__":
    s=input("Enter the String : ")
    s1=most_freq(s)
    for i in s1:
        print(i,"Occurres",s1[i],"times")