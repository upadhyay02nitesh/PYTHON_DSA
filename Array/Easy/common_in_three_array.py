

# def common(s,t,u):
#     s=set(s)
#     t=set(t)
#     u=set(u)

#     c=s.intersection(t)
#     p=list(c.intersection(u))

#     return p

def common(m,n,o,a,b,c):
    l=[]
    last=-897896906
    i,j,k=0,0,0

    while(i<a and j<b and k<c):
        if(m[i]==n[j] and n[j]==o[k]):
            if(last!=m[i]):
                l.append(m[i])
                last=m[i]
            i+=1
            j+=1
            k+=1
        elif (m[i]<n[j]):
            i+=1
        elif (n[j]<o[k]):
            j+=1
        else:
            k+=1
    return l
        


a=int(input("Enter the Number of the input : "))
b=int(input("Enter the Number of the input : "))
c=int(input("Enter the Number of the input : "))

s=list(map(int,input("Enter Element in one line with space ").split()))[:a]
t=list(map(int,input("Enter Element in one line with space ").split()))[:b]
u=list(map(int,input("Enter Element in one line with space ").split()))[:c]
if __name__=="__main__":
    print(common(s,t,u,a,b,c))