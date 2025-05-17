# Stack = last in first out LIFO
# if top element = last element index 

class Stack:
    def __init__(self,n):
        self.stack=[]
        self.top=-1
        # when we insert value then top will increase 
        # when we delete value then top will decrease 
        self.stack_size=n

    def push(self,item):
        if self.top<=self.stack_size-1:
            # because if top=-1 and size =2 then 0,1  max to max top =1
            self.stack.append(item)  
            
            self.top+=1 
        else:
            print("Stack OverFlow!!")

    def pop(self):
        if self.top!=-1:
            # because if top=-1 then no data in stack
            self.stack.pop(0)  
            self.top-=1
        else:
            print("Stack UnderFlow!!")
    def top_element(self):
        return self.stack[self.top]
    def size(self):
        return self.top+1
    
    def display(self):
        print(self.stack)
    
s=Stack(4)
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.display()
print("Stack Size :",s.size())
print("Top Element :",s.top_element())
# s.push(5)
s.pop()
s.pop()
s.display()
s.pop()
s.pop()
s.display()
s.pop()



# 40 top=3
# 30 top=2
# 20 top=1
# 10 top=0
# [] top=-1