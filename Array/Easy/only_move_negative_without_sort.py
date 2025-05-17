def move_element(l,n):
    # j=0
    # for i in range(n):
    #     if l[i]<0:
    #         # temp=l[i]
    #         # l[i]=l[j]
    #         # l[j]=temp
    #         l[i],l[j]=l[j],l[i]
    #         j+=1
    # return l

    
    low,high=0,n-1
    while (low<high):
        if (l[low]<0):
            low+=1
        elif (l[high]>0):
            high-=1
        else:
            l[low],l[high]=l[high],l[low]
    return l
     
    #  2 3 4 -6 -5 4
    #  -5 3 4 -6 2 4
    # -5 -6 4 3 2 4



n=int(input("Enter the Number of the input : "))
l=list(map(int,input("Enter Element in one line with space ").split()))[:n]
if __name__=="__main__":
    print(move_element(l,n))

    
