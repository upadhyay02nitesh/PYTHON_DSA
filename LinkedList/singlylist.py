# in singlylist  nodes are connected with each other 
# 1. Node (value,next node pointer) first node always point start
# if last node (value,null)

class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next

class SLL:
    def __init__(self):
        self.start=None

    def isempty(self):
        return self.start==None
    
    def insert_first(self,value):
        n=Node(value,self.start)
        self.start=n 
    
    def insert_last(self,value):
        n=Node(value,None)
        if self.isempty():
            self.start=n 
        else:
            temp=self.start
            while temp.next!=None:
                temp=temp.next
            temp.next=n 
    
    def insert_particular(self,place,value):
        if not self.isempty():
            temp=self.start
            while temp!=None:
                if temp.item==place:
                    break
                temp=temp.next 
            if temp!=None:
                n=Node(value,temp.next)
                temp.next=n 
            else:
                print("Search element not found !!")

    def search_element(self,value):
        if not self.isempty():
            temp=self.start
            while temp!=None:
                if temp.item==value:
                    return True
                temp=temp.next
            return False
        
    def delete_first(self):
        self.start=self.start.next 
    
    def delete_last(self):
        if not self.isempty():
            if self.start.next==None:
                self.start=None
            else:
                temp=self.start
                prev=temp
                while temp.next!=None:
                    prev=temp
                    temp=temp.next
                prev.next=None
    
    def delete_particular(self,pos):
        if not self.isempty():
            if self.start.item==pos:
                self.start=self.start.next
            # we apply this condition because of self point to next node
            else:
                temp=self.start
                while temp!=None:
                    if temp.item==pos:
                        break
                    prev=temp
                    temp=temp.next
                if temp!=None:
                    prev.next=temp.next
                    temp=None 
                else:
                    print("Element Not Found!!")
                

    
    def display(self):
        temp=self.start
        while temp!=None:
            print(temp.item,end=" ")
            temp=temp.next 
s=SLL()
s.insert_first(10)
s.insert_last(20)
s.display()
print()
s.insert_particular(101,150)
s.insert_particular(10,150)
s.display()
print()
if s.search_element(70)==True:
    print("Item Found")
else:
    print("Not Found!!")

# s.delete_first()
# s.delete_first()
s.display()
print()
print("****")
# s.delete_last()
s.delete_last()
s.display()
print()
s.delete_particular(10)
s.display()
# print(s.start.next.item)
            




        