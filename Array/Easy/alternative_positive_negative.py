
def arranegative_liste(l,n):
    positive_list=[]
    negative_list=[]
    for i in l:
        if i<0:
            negative_list.append(i)
        else:
            positive_list.append(i)
    j,k=0,0
    s=[]
    while (j<len(positive_list) and k<len(negative_list)):
        s.append(positive_list[j])
        s.append(negative_list[k])
        j+=1
        k+=1
    while (j<len(positive_list)):
        s.append(positive_list[j])
        j+=1

    while (k<len(negative_list)):
        s.append(negative_list[k])
        k+=1

    return s



n=int(input("Enter the Number of the input : "))

l=list(map(int,input("Enter Element in one line with space ").split()))[:n]
if __name__=="__main__":
    print(arranegative_liste(l,n))