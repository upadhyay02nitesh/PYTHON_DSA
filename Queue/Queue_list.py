# queue = last in first out FIFO

# enqueue rear+1
# dequeue rear-1
# first value insert yhen front and rear =0 
# if last one  value delete front and rear =-1

class Queue:
    def __init__(self,n):
        self.queue=[]
        self.front=-1
        self.rear=-1
        self.queue_size=n

    def enqueue(self,item):
        if self.rear==-1 and self.front==-1:
            self.queue.append(item)
            self.rear+=1
            self.front+=1

        elif self.rear<self.queue_size-1:
            self.queue.append(item)  
            self.rear+=1 
        else:
            print("queue OverFlow!!")

    def dequeue(self):
        if self.rear>0:
            self.queue.pop(0)  
            self.rear-=1
        elif self.rear==0 and self.front ==0:
            self.queue.pop(0)  
            self.front=-1
            self.rear=-1

        else:
            print("queue UnderFlow!!")
    def front_element(self):
        return self.queue[self.front]
    def rear_element(self):
        return self.queue[self.rear]
    def size(self):
        return self.rear
    
    def display(self):
        print(self.queue)
    
s=Queue(4)
s.enqueue(10)
s.enqueue(20)
s.enqueue(30)
s.enqueue(30)
s.enqueue(40)
s.display()
print("queue Size :",s.size())
print("Front Element :",s.front_element())
print("Rear Element :",s.rear_element())
# s.enqueue(5)
s.dequeue()
s.dequeue()
s.display()
s.dequeue()
s.dequeue()
s.display()
s.dequeue()



# 40 top=3
# 30 top=2
# 20 top=1
# 10 top=0
# [] top=-1