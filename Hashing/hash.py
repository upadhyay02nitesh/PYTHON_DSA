def has_function(key):
    has_key=key%10 
    return has_key

def insert(Hashtable,key,value):
    has_key=has_function(key)
    Hashtable[has_key].append(value)

def display(Hashtable):
    for i in range(len(Hashtable)):
        print(i,end=" ")
        for j in Hashtable[i]:
            print("-->",end=" ")
            print(j,end=" ")
        print()
def search(key):
    for i in range(len(Hashtable)):
        for j in Hashtable[i]:
            if j==key:
                return True
    return False

Hashtable={i:[] for i in range(10)}
insert(Hashtable,10,'kalu')
insert(Hashtable,25,'shankhu')
insert(Hashtable,20,'pinja')
insert(Hashtable,9,'chinki')
insert(Hashtable,21,'minki')
insert(Hashtable,11,'pinki')
display(Hashtable)
print(search('shankhu'))
print(Hashtable)