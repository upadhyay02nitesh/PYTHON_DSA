class PRQ:
    def __init__(self):
        self.l=[]
    
    def isempty(self):
        return len(self.l)==0
    
# We give min element priority in this implementation
    
    def enqueue(self,p,data):
        if self.isempty():
            self.l.append((p,data),)
        else:
            i=0
            while i<len(self.l) and p>self.l[i][0]:
                i+=1 
            self.l.insert(i,(p,data))

            # lets understand 
            # when we insert 1,100 so its empty then self.l=(1,100)


            # when we insert 3,140 then it comes in else block 
            # and intialize i=0 while i<len(l) and p>self.l[i][0]
            # means 0<1 yes and 3>1 yes 
            # i=i+1=1 
            # then  self.l.insert(i,(p,data)) means 3,140 insert into first pos

            # when we insert 2,180 then it comes in else block 
            # and intialize i=0 while i<len(l) and p>self.l[i][0]
            # means 0<2 yes and 2>1 yes 
            # i=i+1=1 

            # again check
            # means 1<2 yes and 2>3 no
            # excution out   
            # then  self.l.insert(i,(p,data)) means 2,180 insert into first pos
            # and 3,140 shift from 2 position

                    
    
    def display(self):
        if not self.isempty():
            print(self.l)
            # for i in self.l:
            #     print(i,end=" ")
    
    def dequeue(self):
        if not self.isempty():
            return self.l.pop(0)
    

p=PRQ()
p.enqueue(1,10)
p.enqueue(3,140)
p.enqueue(2,180)
p.enqueue(5,190)
p.enqueue(4,200)
p.display()
p.dequeue()
p.display()


