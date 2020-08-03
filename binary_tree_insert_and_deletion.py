class Node:
    def __init__(self,key):
        self.left=None
        self.key=key
        self.right=None
def insert(temp,key):
    q=[]
    q.append(temp)
    while len(q)!=0:
        temp=q[0]
        q.pop(0)
        if temp.left==None:
            temp.left=Node(key)
            break
        else:
            q.append(temp.left)
        if temp.right==None:
            temp.right=Node(key)
            break
        else:
            q.append(temp.right)

def rightmost(root,d_node):
    q=[]
    q.append(root)
    while len(q)!=0:
        temp=q
        q.pop(0)
        if temp is d_node:
            temp=None
            return
        if temp.right!=None:
            if temp.right is d_node:
                temp.right=None
                return
            else:
                q.append(tmep.right)
        if temp.left!=None:
            if temp.left is d_node:
                temp.left=None
                return
            else:
                q.append(temp.left)
def delete(root,data):
    if root==None:
        return None
    if root.left==None and root.right==None:
        if root.key==data:
            return None
        else:
            return root
    key_node=None
    q=[]
    q.append(root)
    while len(q)!=0:
        temp=q
        q.pop(0)
        if temp.key==data:
            key_node=temp
        if temp.left!=None:
            q.append(temp.left)
        if tep.right!=None:
            q.append(temp.right)
    if key_node!=None:
        x=temp.key
        rightmost(root,temp)
        key_node.key=x
    return root
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
insert(root,4)
delete(root,6)
