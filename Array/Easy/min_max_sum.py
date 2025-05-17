def sum_min_max(l,n):
    if n==1:
        return l[0]
    if l[0]>l[1]:
        max=l[0]
        min=l[1]
    else:
        max=l[1]
        min=l[0]
    for i in range(2,n):
        if l[i]>max:
            max=l[i]
        elif l[i]<min:
            min=l[i]
    # print(max,min)
    return max+min

n=int(input("Enter how Many element : "))
l=list(map(int, input("Enter numbers separated by spaces: ").split()))[:n]
print(l)
if __name__=="__main__":
    print(sum_min_max(l,n))