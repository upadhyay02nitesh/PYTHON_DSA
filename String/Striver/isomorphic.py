
def isomorphic(s,t):
    if len(s)!=len(t):
        return False
    st={}
    ts={}
    for i,j in zip(s,t):
        
        if i in st:
            if st[i]!=j:
                return False
        else:
            st[i]=j
        if j in ts:
            if ts[j]!=i:
                return False
        else:
            ts[j]=i
    # print(st)
    # print(ts)
    return True

    


    
if __name__=="__main__":
    s=input("Enter String : ")
    t=input("Enter String : ")

    print(isomorphic(s,t))