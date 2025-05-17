
def anagram(s,t):
    # if len(s)!=len(t):
    #     return False
    # return sorted(s)==sorted(t)


    if len(s)!=len(t):
        return False
    else:
        maps={}
        mapt={}
        for i in s:
            maps[i]=maps.get(i,0)+1
        for j in t:
            mapt[j]=mapt.get(j,0)+1
        # print(mapt)
        # print(maps)
        return maps==mapt
    
    
    

if __name__=="__main__":
    s=input("Enter String : ")
    t=input("Enter String : ")

    print(anagram(s,t))