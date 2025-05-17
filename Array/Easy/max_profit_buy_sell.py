

# def max_profit(l,n):
#     profit=0
#     for i in range(n):
#         buy=l[i]
#         for j in range(i+1,n):
#             cur_profit=l[j]-buy 
#             # print("Buy day :",i+1,"sell day :",j+1,"profit=",cur_profit)
#             if cur_profit>profit:
#                 profit=cur_profit
#             cur_profit=0
#     return profit


def max_profit(l,n):
    buy=l[0]
    profit=0
    for i in range(n):
        if l[i]<buy:
            buy=l[i]
            # print("minimum buy",buy)
        elif l[i]-buy>profit:
            profit=l[i]-buy 
            # print("when selling point",l[i])
            # print("max profit",profit)

    return profit





n=int(input("Enter the Number of sum : "))
l=list(map(int,input("Enter Element in one line with space ").split()))[:n]
if __name__=="__main__":
    print(max_profit(l,n))