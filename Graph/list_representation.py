class Graph:
    def __init__(self,vno):
        self.vertex=vno 
        self.adj_dict={v:[] for v in range(vno)}
    def add_edge(self,u,v):
        if 0<=u<self.vertex and 0<=v<self.vertex:
            self.adj_dict[u].append(v)
            self.adj_dict[v].append(u)
        else:
            print("Provide valid Vertices !!!")

    def remove_edge(self,u,v):
        if 0<=u<self.vertex and 0<=v<self.vertex:
            self.adj_dict[u].remove(v)
            self.adj_dict[v].remove(u)
        else:
            print("Provide valid Vertices !!!")
    def has_edge(self,u,v):
        if 0<=u<self.vertex and 0<=v<self.vertex:
            for i in self.adj_dict[u]:
                if v==i:
                    return True
            return False
        else:
            print("Provide valid Vertices !!!")
    def print_edge(self):
        for i in range(self.vertex):
            print("V"+str(i),"-->",end=" ")
            print("V",self.adj_dict[i],end=" ")
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