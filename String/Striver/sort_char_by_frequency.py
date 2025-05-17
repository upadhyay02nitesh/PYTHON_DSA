from collections import Counter
def sort_frequency(s):
    freq=Counter(s)
    # print(freq.items())
    sorted_frequency=sorted(freq.items(),key=lambda x:x[1],reverse=True)
    # print(sorted_frequency)
    result="".join(i*j for i,j in sorted_frequency)
    return result
    


    
if __name__=="__main__":
    s=input("Enter String : ")
    print(sort_frequency(s))