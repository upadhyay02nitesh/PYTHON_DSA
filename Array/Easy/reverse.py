# def rev(l):
#     l=l[::-1]
#     return l
    
# l=list(map(int, input("Enter numbers separated by spaces: ").split()))
# if __name__=="__main__":
#     print(rev(l))



# def rev(l):
#     s=[]
#     for i in range(len(l)-1,-1,-1):
#         s.append(l[i])
#     return s
    
    
# l=list(map(int, input("Enter numbers separated by spaces: ").split()))
# if __name__=="__main__":
#     print(rev(l))

def rev(l):
    l.reverse()
    return l
    
    
l=list(map(int, input("Enter numbers separated by spaces: ").split()))
if __name__=="__main__":
    print(rev(l))



