def union_sort(n,m,s,t):
    # s=set(s)
    # t=set(t)
    # p=s.union(t)
    # return sorted(p)

    sort_arr=[]
    i,j=0,0
    last=-345
    while i<n and j<m:
        if s[i]<t[j]:
            if s[i]!=last:
                sort_arr.append(s[i])
                last=s[i]
            i+=1
        elif s[i]>t[j]:
            if t[j]!=last:
                sort_arr.append(t[j])
                last=t[j]
            j+=1
        else:
            if s[i]!=last:
                sort_arr.append(s[i])
                last=s[i]
            i+=1
            j+=1

    while i<n:
        if s[i]!=last:
                sort_arr.append(s[i])
                last=s[i]
        i+=1
    
    while j<m:
        if t[j]!=last:
                sort_arr.append(t[j])
                last=t[j]
        j+=1
    return sort_arr




if __name__=="__main__":
    n=int(input("Enter how mny element you :"))
    m=int(input("Enter how mny element you :"))
    s=list(map(int,input("Enter element in space ").split()))
    t=list(map(int,input("Enter element in space ").split()))
    s.sort()
    print(union_sort(n,m,s,t))