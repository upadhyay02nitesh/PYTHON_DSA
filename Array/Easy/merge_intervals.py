
def merge_intervals(mat):
    mat.sort()
    ans=[]

    for [x,y] in mat:
        if not ans or ans[-1][1]<x:
            ans.append([x,y])
        elif ans[-1][1]<y:
            ans[-1][1]=y 
    return ans

n=int(input("Enter the Number of the input : "))
m=int(input("Enter the Number of the input : "))
mat=[]
for i in range(n):
    row=[]
    for j in range(m):
        row.append(int(input("Enter element : ")))
    mat.append(row)

if __name__=="__main__":
    ans=merge_intervals(mat)
    print(ans)
    