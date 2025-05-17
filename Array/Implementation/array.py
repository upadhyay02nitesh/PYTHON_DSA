class Array:
    def __init__(self):
        self.array=[]
    def isempty(self):
        return len(self.array)==0
    def insertfirst(self,value):
        if self.isempty():
            self.array.append(value)
        else:
            self.array.insert(0,value)
    
    def insertlast(self,value):
        self.array.insert(0,value)
    
    def deletefirst(self):
        if not self.isempty():
            self.array.pop(0)
        else:
            return "No element to delete"
        
    def deletelast(self):
        if not self.isempty():
            self.array.pop()
        else:
            return "No element to delete"
    
    def display(self):
        if not self.isempty():
            for i in self.array:
                print(i,end=" ")
        else:
            return "No element in the array"

a=Array()
a.insertfirst(10)
a.insertfirst(100)
a.insertlast(20)
a.insertfirst(60)
a.display()
print()
a.deletefirst()
a.display()
a.deletelast()
print()
a.display()
    
        


