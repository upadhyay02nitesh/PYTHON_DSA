

class Node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev=prev
        self.item=item
        self.next=next 

class DDQ:
    def __init__(self):
        self.front=None
        self.rear=None
    
    def isempty(self):
        return self.front==None 
    
    def insert_first(self,data):
        n=Node(None,data,None)
        if self.isempty():
            self.front=n
            self.rear=n 
        else:
            n.next=self.front 
            self.front.prev=n 
            self.front=n 

    def insert_last(self,data):
        n=Node(None,data,None)
        if self.isempty():
            self.front=n
            self.rear=n 
        else:
            temp=self.front 
            while temp.next!=None:
                temp=temp.next 
            n.prev=temp 
            temp.next=n 
            self.rear=n 

    def delete_first(self):
        if not self.isempty():
            if self.front.next!=None:
                self.front.next.prev=None 
                self.front=self.front.next 

            else:
                self.front=None  
                self.rear=None

    def delete_last(self):
        if not self.isempty():
            if self.front.next!=None:
                temp=self.front
                while temp.next!=None:
                    temp=temp.next
                temp.prev.next=None
                self.rear=temp.prev
            else:
                self.front=None  
                self.rear=None
    def display(self):
        if not self.isempty():
            temp=self.front
            while temp!=None:
                print(temp.item,end=" ")
                temp=temp.next 

d=DDQ()
d.insert_first(10)
d.insert_first(20)
d.insert_last(30)
d.insert_last(40)
d.display()
print()
d.delete_first()
d.display()
print()
d.delete_last()
d.display()
# print()
# print(d.front.item)
# print(d.rear.item)




                







d=DDQ()
d.insert_first(10)
d.insert_last(20)


