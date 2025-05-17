class Node:
    def __init__(self,left=None,item=None,right=None):
        self.left=left
        self.item=item 
        self.right=right 
class BST:
    def __init__(self):
        self.root=None 
    def insert(self,data):
        self.root=self.rinsert(self.root,data)
    def rinsert(self,root,data):
        n=Node(item=data)
        if root is None:
            return n
        if data<root.item:
            root.left=self.rinsert(root.left,data)
        elif data>root.item:
            root.right=self.rinsert(root.right,data)
        return root 
    
    def search(self,data):
        return self.rsearch(self.root,data)
    def rsearch(self,root,data):
        if root is None or root.item==data:
            return root
        if data<root.item:
            return self.rsearch(root.left,data)
        elif data>root.item:
            return self.rsearch(root.right,data)
    
    def inorder(self):
        result=[]
        self.rinorder(self.root,result)
        return result
    def rinorder(self,root,result):
        if root:
            self.rinorder(root.left,result)
            result.append(root.item)
            self.rinorder(root.right,result)


    def preorder(self):
        result=[]
        self.rpreorder(self.root,result)
        return result
    def rpreorder(self,root,result):
        if root:
            result.append(root.item)
            self.rpreorder(root.left,result)
            self.rpreorder(root.right,result)


    def postorder(self):
        result=[]
        self.rpostorder(self.root,result)
        return result
    def rpostorder(self,root,result):
        if root:
            self.rpostorder(root.left,result)
            self.rpostorder(root.right,result)
            result.append(root.item)
    def min_value(self,temp):
        curr=temp 
        while curr.left!=None:
            curr=curr.left 
        return curr.item
    
    def max_value(self,temp):
        curr=temp 
        while curr.right!=None:
            curr=curr.right
        return curr.item

    def delete(self,data):
        self.root=self.rdelete(self.root,data)
    
    def rdelete(self,root,data):
        if root is None:
            return root
        if data<root.item:
            root.left=self.rdelete(root.left,data)
        elif data>root.item:
            root.right=self.rdelete(root.right,data)
        else:
            if root.left is None:
                return root.right 
            elif root.right is None:
                return root.left 
            else:
                root.item=self.min_value(root.right)
                # root.item=self.max_value(root.left)
                self.rdelete(root.right,root.item)
        return root 

b=BST()
b.insert(10)
b.insert(5)
b.insert(15)
b.insert(25)
b.insert(12)
b.insert(13)
b.insert(35)
b.insert(17)
b.insert(40)
print(b.inorder())
print(b.preorder())
print(b.postorder())
s=b.search(15)
if s!=None:
    print("Find")
else:   
    print("Not Find")
b.delete(15)
print(b.inorder())