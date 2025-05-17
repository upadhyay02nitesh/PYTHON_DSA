from collections import Counter
def most_occurrence(l,n,k):
    x=n//k 
    c=0
    l1=[]
    # l1={}
    for i in l:
        if i not in l1:
            c=l.count(i)
            if c>x:
                l1.append(i)
            # l1.update({i:c})


    
    # l1=Counter(l)
    # l1=dict(l1)
            
    # return l1
    

n=int(input("Enter the Number of the input : "))
k=int(input("Enter the Number of the input : "))

l=list(map(int,input("Enter Element in one line with space ").split()))[:n]

if __name__=="__main__":
    print(most_occurrence(l,n,k))