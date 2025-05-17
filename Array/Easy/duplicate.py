
def duplicate(l,n):
    l.sort()
    s=[]
    for i in range(1,n):
        if l[i-1]==l[i]:
            s.append(l[i])
    return s



    # s=[]
    # j=[]
    # for i in l:
    #     if i not  in s:
    #         s.append(i)
    #     else:
    #         if i not in j:
    #           j.append(i)
    # return j



    # s=[]
    # for i in l:
    #     if l.count(i)>1:
    #         if i not in s:
    #             s.append(i)
    # return s



n=int(input("Enter the Number of the input : "))

l=list(map(int,input("Enter Element in one line with space ").split()))[:n]
if __name__=="__main__":
    print(duplicate(l,n))