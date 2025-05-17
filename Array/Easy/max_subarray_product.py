def max_product(l,n):
    max_product=l[0]
    cur_product=l[0]


    for i in range(1,n):
        cur_product*=l[i]
        # print(cur_product)

        if cur_product>max_product:
            max_product=cur_product

    return max_product


n=int(input("Enter the Number of the input : "))
l=list(map(int,input("Enter Element in one line with space ").split()))[:n]
if __name__=="__main__":
    print(max_product(l,n))