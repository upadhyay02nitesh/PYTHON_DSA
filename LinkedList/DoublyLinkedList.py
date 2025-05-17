class Node:
    def __init__(self, prev=None, item=None, next=None):
        self.prev = prev
        self.item = item
        self.next = next

class DLL:
    def __init__(self):
        self.start = None

    def isempty(self):
        return self.start is None

    def insert_first(self, item):
        n = Node(None, item, None)
        if self.isempty():
            self.start = n
        else:
            n.next = self.start
            self.start.prev = n
            self.start = n

    def insert_last(self, item):
        n = Node(None, item, None)
        if self.isempty():
            self.start = n
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            n.prev = temp
            temp.next = n

    def insert_particular(self, pos, item):
        if not self.isempty():
            n = Node(None, item, None)
            temp = self.start
            while temp is not None:
                if temp.item == pos:
                    break
                temp = temp.next
            if temp is not None:
                n.prev = temp
                n.next = temp.next
                if temp.next is not None:
                    temp.next.prev = n
                temp.next = n
            else:
                print("Position element not found")

    def search_element(self, ele):
        if not self.isempty():
            temp = self.start
            while temp is not None:
                if temp.item == ele:
                    break
                temp = temp.next
            if temp is not None:
                print(temp.item, "Find the element")
            else:
                print("No Find")

    def delete_first(self):
        if not self.isempty():
            if self.start.next is not None:
                self.start.next.prev = None
            self.start = self.start.next

    def delete_last(self):
        if not self.isempty():
            if self.start.next is None:  # Only one element
                self.start = None
            else:
                temp = self.start
                while temp.next is not None:
                    temp = temp.next
                temp.prev.next = None
    def delete_particular(self,value):
        if not self.isempty():
            if self.start.next==None:
                if self.start.item==value:
                    self.start=None
            else:
                temp=self.start
                while temp!=None:
                    if temp.item==value:
                        break
                    temp=temp.next 
                if temp!=None:
                    if temp==self.start:
                        self.start.next.prev=None
                        self.start=self.start.next
                    else:
                        temp.prev.next=temp.next


    def display(self):
        if not self.isempty():
            temp = self.start
            while temp is not None:
                print(temp.item, end=" ")
                temp = temp.next
            
        else:
            print("List is empty")

# Example usage:
d = DLL()
d.insert_first(10)
d.insert_first(20)
d.insert_last(100)
d.display()
print()
d.insert_particular(20, 200)
d.display()
print()
d.search_element(1000)
d.delete_first()
print()
d.display()
d.delete_last()
print()
print("**")
d.display()
d.delete_particular(200)
print()
print("**")
d.display()
print()
# print(d.start.item)
# print()
