# Create SinglyLinkedList Perfotm LIFO Operation
class Node:
    def __init__(self,item=None,next=None):
        self.item=item 
        self.next=next 
class SLL_Stack:
    def __init__(self):
        self.start=None 
    
    def isempty(self):
        return self.start==None
    
    def push(self,value):
        if self.isempty():
            n=Node(value,self.start)
            self.start=n 
        else:
            temp=self.start
            while temp.next!=None:
                temp=temp.next 
            n=Node(value,None)
            temp.next = n 

    def pop(self):
        if not self.isempty():
            self.start=self.start.next 
    def display(self):
        if not self.isempty():
            temp=self.start
            while temp!=None:
                print(temp.item,end=" ")
                temp=temp.next 
s=SLL_Stack()
s.push(10)
s.push(20)
s.push(30)
s.display()
s.pop()
print()
s.display()
s.pop()
print()
s.display()