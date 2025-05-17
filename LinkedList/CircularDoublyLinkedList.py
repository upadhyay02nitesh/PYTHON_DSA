class Node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev=prev
        self.item=item
        self.next=next

class DSL:
    def __init__(self):
        self.start=None 
    def isempty(self):
        return self.start==None 
    def insert_start(self,data):
        n=Node()
        n.item=data 
        if self.isempty():
            n.prev=n 
            n.next=n 
            self.start=n 
        else:
            if self.start!=self.start.next:
                n.next=self.start
                n.prev=self.start.prev 
                self.start.prev=n
                self.start.prev.next=n 

            else:
                n.next=self.start
                n.prev=self.start
                self.start.prev=n 
                self.start.next=n 
            self.start=n
    def insert_last(self,data):
        n=Node()
        n.item=data 
        if self.isempty():
            n.prev=n 
            n.next=n 
            self.start=n
        else:
            if self.start!=self.start.next:
                n.prev=self.start.prev 
                n.next=self.start
                self.start.prev.next=n 
                self.start.prev=n 
            else:
                n.prev=self.start
                n.next=self.start 
                self.start.prev=n

    def insert_particular(self,pos,data):
        if not self.isempty():
            n=Node()
            n.item=data 
            if self.start.item==pos:
                if self.start!=self.start.next:
                    n.prev=self.start 
                    n.next=self.start.next 
                    self.start.next=n 
                else:
                    n.prev=self.start
                    n.next=self.start 
                    self.start.next=n 
            else:
                temp=self.start.next 
                while temp!=self.start:
                    if temp.item==pos:
                        break
                    temp=temp.next 
    def display(self):
        if not self.isempty():
            temp = self.start
            print(temp.item, end=" ")
            temp = temp.next
            while temp != self.start:
                print(temp.item, end=" ")
                temp = temp.next
    
    def search(self,data):
        if not self.isempty():
            temp=self.start
            if temp.item==data:
                return True
            temp=temp.next
            while temp!=self.start:
                if temp.item==data:
                    return True
                temp=temp.next 
        return False

    def delete_start(self):
        if not self.isempty():
            if self.start!=self.start.next:
                if self.start.prev!=self.start.next:
                    self.start.next.prev=self.start.prev 
                    self.start.prev.next=self.start.next
                else:
                    self.start.next.prev=self.start.next
                    self.start.next.next=self.start.next
                self.start=self.start.next
            else:
                self.start=None
    def delete_last(self):
        if not self.isempty():
            if self.start!=self.start.next:
                if self.start.prev!=self.start.next:
                    self.start.prev.prev.next=self.start
                    self.start.prev=self.start.prev.prev 
                    
                else:
                    self.start.next=self.start
                    self.start.prev=self.start
            
            else:
                self.start=None
    def delete_particular(self,data):
        if not self.isempty():
            temp=self.start
            if temp.item==data:
                if self.start!=self.start.next:
                    if self.start.prev!=self.start.next:
                        self.start.next.prev=self.start.prev 
                        self.start.prev.next=self.start.next
                    else:
                        print("hi")
                        self.start.next.prev=self.start.next
                        self.start.next.next=self.start.next
                    self.start=self.start.next
                
                else:
                    self.start=None
                return
            temp=temp.next 
            while temp!=self.start:
                if temp.item==data:
                    break
                temp=temp.next
            if temp!=self.start:
                if temp==self.start.prev:
                    if self.start.prev==self.start.next:
                        self.start.prev=self.start 
                        self.start.next=self.start
                    else:
                        self.start.prev=self.start.prev.prev
                        self.start.prev.prev.next=self.start
                else:
                    print()
                    # print(temp.prev.prev.item)
                    temp.next.prev=temp.prev 
                    temp.prev.next=temp.next
                    temp=None

            else:
                print("Item Does Not Found")

                    
            
s=DSL()
s.insert_start(10)
s.insert_start(20)
s.insert_last(30)
# s.insert_particular(20,50)
# print(s.start.next.item)
print()
s.display()
print()
# s.delete_start()
print(s.search(30))
s.display()
print()
# s.delete_last()
s.display()
print()
# print(s.start.item)
s.delete_particular(30)
# s.delete_particular(10)
# s.delete_particular(20)
print()
s.display()


