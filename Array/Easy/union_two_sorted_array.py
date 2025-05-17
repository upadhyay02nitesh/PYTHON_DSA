def union_array(l,s):
    # l=set(l)
    # s=set(s)
    # c=l.union(s)
    # return len(c)
    c=set()
    for i in l:
        c.add(i)
    for i in s:
        c.add(i)
    return len(c)



n=int(input("Enter the Number of the input : "))
m=int(input("Enter the Number of the input : "))
l=list(map(int,input("Enter Element in one line with space ").split()))[:n]
s=list(map(int,input("Enter Element in one line with space ").split()))[:n]
if __name__=="__main__":
    print(union_array(l,s))