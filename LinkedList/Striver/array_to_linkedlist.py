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
    def display(self,head):
        temp=head
        while temp.next!=None:
            print(temp.data,end="->")
            temp=temp.next
        print(temp.data)
l=LL()
s=l.construct([1,2,3,4,5])
l.display(s)


        
            


