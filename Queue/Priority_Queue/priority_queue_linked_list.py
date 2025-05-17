class Node:
    def __init__(self,prior=None,item=None,next=None):
        self.prior=prior 
        self.item=item 
        self.next=next
class SPRQ:
    def __init__(self):
        self.start=None
    
    def isempty(self):
        return self.start==None
    
    def enqueue(self,prior,data):
        n=Node(prior,data)
        if self.isempty() or prior<=self.start.prior:
            n.next=self.start
            self.start=n 
        else:
            temp=self.start 
            while temp.next!= None and prior>=temp.next.prior:
                temp=temp.next 
            n.next=temp.next 
            temp.next=n 

    def dequeue(self):
        if not self.isempty():
            self.start=self.start.next 
    
    def display(self):
        if not self.isempty():
            temp=self.start
            while temp!=None:
                print(temp.item,end=" ")
                temp=temp.next

s=SPRQ()
s.enqueue(1,100)
s.enqueue(3,200)
s.enqueue(2,300)
s.display()
print()
s.dequeue()
s.display()



# Lets Understand the logic 

# Node(data,prior,next)

# enqueue- in this we check if isempty and if priority less than starting 
# element then point start = this Data 

# if not empty then priority > last element then last = this element 

# for delete delete first element
