# Create SinglyLinkedList Perfotm FIFO Operation

# for insert we use rear for delete we use front
class Node:
    def __init__(self,item=None,next=None):
        self.item=item 
        self.next=next 
class SLL_Queue:
    def __init__(self):
        self.front=None 
        self.rear=None 
        #in first insertion front rear both point first node then rear point next node 
        #in delete when both front and rear point first node then both should be none
    
    def isempty(self):
        return self.front==None
    
    #we can insert row wise means insert at last but we have rear so using this
    # we didnot implement insert and end concept
    def Enqueue(self,value):
        if self.front==None:
            n=Node(value,self.rear)
            self.front=n 
            self.rear=n 
        else:
            n=Node(value,None)
            self.rear.next=n
            self.rear=n


    def dequeue(self):
        if not self.isempty():
            if self.rear==self.front:
                self.rear=None 
                self.front=None 
            else:
                self.front=self.front.next
    def display(self):
        if not self.isempty():
            temp=self.front
            while temp!=None:
                print(temp.item,end=" ")
                temp=temp.next 
s=SLL_Queue()
s.Enqueue(10)
s.Enqueue(20)
s.Enqueue(30)
print("Front Item :",s.front.item)
print()
print("Rear Item :",s.rear.item)
print()
s.display()
s.dequeue()
print()
s.display()
s.dequeue()
print()
s.display()
