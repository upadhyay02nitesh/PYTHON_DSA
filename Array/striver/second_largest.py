
def second_largest_element(s):
    max=-1
    second_max=-1
    for i in s:
        if i>max:
            second_max=max 
            # print("Sec",second_max)
            max=i
        elif i>second_max and i!=max:
            second_max=i

            # print("sec",second_max)
   
    return second_max


    
if __name__=="__main__":
    n=int(input("Enter how mny element you "))
    s=list(map(int,input("Enter element in space ").split()))
    print(second_largest_element(s))