class Graph:
    def __init__(self,vno):
        self.vertex_no=vno
        self.adj_matrix=[[0]*vno for i in range(vno)]
    def add_edge(self,u,v,weight=1):
        if 0<=u<self.vertex_no and 0<=v<self.vertex_no:
            self.adj_matrix[u][v]=weight
            self.adj_matrix[v][u]=weight
        else:
            print("Provide valid vertice !!")
    def remove_edge(self,u,v):
        if 0<=u<self.vertex_no and 0<=v<self.vertex_no:
            self.adj_matrix[u][v]=0
            self.adj_matrix[v][u]=0
        else:
            print("Provide valid vertice !!")

    def has_edge(self,u,v):
        if 0<=u<self.vertex_no and 0<=v<self.vertex_no:
            return self.adj_matrix[u][v]!=0
        else:
            print("Provide valid vertice !!")

    
    def print_edge(self):
        print("   V0 V1 V2 V3 V4")
        for i in range(self.vertex_no):
            print("V"+str(i),end=" ")
            for j in range(len(self.adj_matrix[i])):
                print(self.adj_matrix[i][j],end="  ")
            print()
g=Graph(5)
g.add_edge(0,1)
g.add_edge(1,2)
g.add_edge(3,4)
g.add_edge(2,3)
g.print_edge()
print(g.has_edge(1,2))
g.remove_edge(0,1)
g.print_edge()
