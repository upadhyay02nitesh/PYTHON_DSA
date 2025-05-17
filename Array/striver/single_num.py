def single_num(n,s):
    result=0
    for num in s:
        result=result^num 
        # print(result)
    return result

    

if __name__=="__main__":
    n=int(input("Enter how mny element you :"))
    s=list(map(int,input("Enter element in space ").split()))
    print(single_num(n,s))