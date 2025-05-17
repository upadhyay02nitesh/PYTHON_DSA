
def roate(s,t):
    if len(s)!=len(t):
        return False
    # temp=s+s 
    # if (temp.count(t)>0):
    #     return True
    # return False

    return t in (s+s)
    



    
if __name__=="__main__":
    s=input("Enter String : ")
    t=input("Enter String : ")

    print(roate(s,t))