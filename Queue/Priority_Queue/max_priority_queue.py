class PRQ:
    def __init__(self):
        self.l=[]
    
    def isempty(self):
        return len(self.l)==0
    
# We give max element priority in this implementation
    
    def enqueue(self,p,data):
        if self.isempty():
            self.l.append((p,data),)
        else:
            for i in range(len(self.l)):
                if p>=self.l[i][0]:
                    break
            self.l.insert(i,(p,data))


                    
    
    def display(self):
        if not self.isempty():
            print(self.l)
            # for i in self.l:
            #     print(i,end=" ")
    
    def dequeue(self):
        if not self.isempty():
            return self.l.pop(0)
    

p=PRQ()
p.enqueue(1,10)
p.enqueue(3,140)
p.enqueue(2,180)
p.enqueue(5,190)
p.enqueue(4,200)
p.display()
p.dequeue()
p.display()


