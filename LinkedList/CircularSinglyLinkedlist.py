class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
    
class CSL:
    def __init__(self):
        self.last=None
    
    def isempty(self):
        return self.last==None
    
    def insert_start(self,data):
        n=Node(data)
        if self.isempty():
            n.next=n 
            self.last=n 
        else:
            n.next=self.last.next 
            self.last.next=n 
           
    
    def insert_last(self,data):
        n=Node(data)
        if self.isempty():
            n.next=n 
            self.last=n
        else:
            n.next=self.last.next 
            self.last.next=n 
            self.last=n 
    def insert_particular(self,data,pos):
        if not self.isempty():
            n=Node(data)
            temp=self.last.next
            while temp!=self.last:
                if temp.item==pos:
                    break
                temp=temp.next 
                
            if self.last.item==pos:
                n.next=self.last.next 
                self.last.next=n 
                self.last=n 
            else:
                if temp.item==pos:
                    n.next=temp.next
                    temp.next=n 
                else:
                    print("Position Not Found")

    def display(self):
        if not self.isempty():
            temp=self.last.next 
            while temp!=self.last:
                print(temp.item,end=" ")
                temp=temp.next 
            print(self.last.item)

    def search(self,data):
        if not self.isempty():
            temp=self.last.next 
            while temp!=self.last:
                if temp.item==data:
                    return True
                temp=temp.next 
            if self.last.item==data:
                return True
        return False
    
    def delete_first(self):
        if not self.isempty():
            if self.last.next==self.last:
                self.last=None
            else:
                self.last.next=self.last.next.next
    
    def delete_last(self):
        if not self.isempty():
            if self.last.next==self.last:
                self.last=None
            elif self.last.next==self.last.next.next.next:
                self.last.next.next=self.last.next 
                self.last=self.last.next
            else:
                temp=self.last.next 
                prev=temp
                while temp!=self.last:
                    prev=temp
                    temp=temp.next
                prev.next=temp.next  #we can write temp=self.last because point self.last
                self.last=prev
    def delete_particular(self, data):
        if self.isempty():
            print("List is empty")
            return
        
        if self.last.next == self.last:  # Single node case
            if self.last.item == data:
                self.last = None
            else:
                print("Data not found")
            return
        
        # Multiple nodes case
        temp = self.last.next  # Start from the first node
        prev = self.last  # Start prev from the last node
        
        while temp != self.last:  # Traverse the list
            if temp.item == data:
                break
            prev = temp
            temp = temp.next
        
        if temp != self.last:  # Node to delete is not the last node
            prev.next = temp.next  # it also handle delete fron first node
        else:
            if temp.item == data:  # Node to delete is the last node
                prev.next = temp.next
                self.last = prev
            else:
                print("Data not found")
                    



c=CSL()
c.insert_start(10)
c.insert_last(20)
c.insert_start(100)
# print(c.last.item)
c.insert_particular(200,10)
# c.insert_particular(207,16)
c.display()
print(c.search(10))
print(c.search(109))
print()
# c.delete_first()
# c.display()
# print()
# c.delete_last()
c.display()
print()
c.delete_last()
c.display()
print()
c.delete_particular(100)
c.display()
# print(c.last.item)

