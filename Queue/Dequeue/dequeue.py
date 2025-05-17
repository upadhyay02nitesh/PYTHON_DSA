class Dequeue:
    def __init__(self):
        self.l=[]

    def isempty(self):
        return  len(self.l)==0
    
    def enqueuefirst(self,data):
        self.l.insert(0,data)
    def enqueuelast(self,data):
        self.l.append(data)
    def dequeuefirst(self):
        if not self.isempty():
            self.l.pop(0)
    def dequeuelast(self):
        if not self.isempty():
            self.l.pop()
    def display(self):
        if not self.isempty():
            print(self.l)
    
d=Dequeue()
d.enqueuefirst(10)
d.enqueuefirst(20)
d.enqueuelast(30)
d.enqueuelast(40)
d.display()
print()
d.dequeuefirst()
d.dequeuelast()
d.display()
print()
