
def subset(l,l1):
    # l=set(l)
    # l1=set(l1)
    # return l1.issubset(l)

    for i in l1:
        if i in l:
            continue
        else:
            return False
    return True 


n=int(input("Enter the Number of the input : "))
m=int(input("Enter the Number of the input : "))

l=list(map(int,input("Enter Element in one line with space ").split()))[:n]
l1=list(map(int,input("Enter Element in one line with space ").split()))[:m]
if __name__=="__main__":
    print(subset(l,l1))