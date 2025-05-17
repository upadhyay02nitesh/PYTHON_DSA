# def sorted_rotated_array(n,s):
#     if n==1:
#         return True
#     count=0
#     for i in range(n):
#         # 3 4 5 1 2
#         # (i+1)%n because when i=4 (4+1)%n =0 s[4]>s[0]
#         if s[i]>s[(i+1)%n]:  #3 4 5 1 2 here only 5>1 only one true so its rotated and sorted
#             count+=1
#     return count<=1


# if __name__=="__main__":
#     n=int(input("Enter how mny element you "))
#     s=list(map(int,input("Enter element in space ").split()))
#     print(sorted_rotated_array(n,s))


def lenOfLongSubarr (arr, n, k) : 
        current=0
        max=0
        for i in range(n):
            cur_sum=arr[i]
            for j in range(i+1,n):
                cur_sum+=arr[j]
                current+=1
                if cur_sum==k:
                    if current>max:
                        max=current
                        print(max)
                        current=0
        
        return max
print(lenOfLongSubarr([1,4,3,2,5,5],6,15))