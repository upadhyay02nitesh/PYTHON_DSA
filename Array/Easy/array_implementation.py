class Array:
    def __init__(self):
        self.array=[]
    def is_empty(self):
        return len(self.array)==0
    def insert_first(self,data):
        if not self.is_empty():
            self.array.insert(0,data)
        else:
            self.array.append(data)
    def insert_last(self,data):
        self.array.append(data)
    def insert_particular(self,data,pos):
        if not self.is_empty():
            self.array.insert(pos,data)
        else:
            print("Array Is Empty!!")
    
    def display(self):
        if not self.is_empty():
            for i in self.array:
                print(i,end=" ")
        else:
            print("Array Is Empty!!")
    
    def delete_first(self):
        if not self.is_empty():
            self.array.pop(0)
        else:
            print("Array Is Empty!!")
    def delete_last(self):
        if not self.is_empty():
            self.array.pop()
        else:
            print("Array Is Empty!!")
    def delete_particular(self,data):
        self.array.remove(data)
    
a=Array()
a.insert_first(10)
a.insert_last(20)
a.insert_particular(30,1)
a.display()
print()
a.delete_first()
a.display()
print()
a.delete_particular(20)
a.display()
print()
a.delete_last()
a.display()
print()
