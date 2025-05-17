class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LL:
    def construct(self,arr):
        if not arr:
            return None
        head=Node(arr[0])
        current=head 
        for val in arr[1:]:
            current.next=Node(val)
            current=current.next
        return head
    
    def insert_at_end(self,head,x):
        n=Node(x)
        if head is not None:
            temp=head 
            while temp.next!=None:
                temp=temp.next
            temp.next=n
        else:
            head=n 
        return head
    def insert_at_start(self,head,x):
        n=Node(x)
        if head is not None:
            n.next=head
            head=n 
        else:
            head=n 
        return head
    def length(self,head):
        temp=head
        c=0
        while temp!=None:
            c+=1
            temp=temp.next
        return c
        
    def insert_at_pos(self,head,pos,x):
        n=Node(x)
        if head is not None:
            c=1
            temp=head
            cur=temp
            while temp!=None:
                if c==pos:
                    break
                cur=temp
                temp=temp.next
                c+=1
            if temp!=None:
                if c==1:
                    n.next=head 
                    head=n 
                else:
                    n.next=cur.next 
                    cur.next=n
            else:
                print("Position not found !!")
 
        return head

                
    def display(self,head):
        temp=head
        while temp.next!=None:
            print(temp.data,end="->")
            temp=temp.next
        print(temp.data)
l=LL()
s=l.construct([1,2,3,4,5])
# print(l.length(s))
# l.insert_at_end(s,6)
# l.display(s)
# so=l.insert_at_start(s,98)
# l.display(so)
siii=l.insert_at_pos(s,1,45)
l.display(siii)


        
            


