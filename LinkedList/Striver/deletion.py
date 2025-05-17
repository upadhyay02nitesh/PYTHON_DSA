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
    
    def length(self,head):
        temp=head
        c=0
        while temp!=None:
            c+=1
            temp=temp.next
        return c
    def delete_given_node(self,head,pos_ele):
        if head is not None:
            temp=head 
            cur=temp
            while temp!=None:
                if temp.data==pos_ele:
                    break
                cur=temp
                temp=temp.next 
            if temp!=None:
                if temp.data==head.data:
                    head=head.next 
                else:
                    cur.next=cur.next.next
            else:
                print("data nor found")
        return head
                
    def display(self,head):
        temp=head
        while temp.next!=None:
            print(temp.data,end="->")
            temp=temp.next
        print(temp.data)
l=LL()
s=l.construct([1,2,3,4,5])

# l.display(s)
s1=l.delete_given_node(s,1)
l.display(s1)


        
            


