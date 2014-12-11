
# coding: utf-8

# In[1]:

from time import time

# linear search
def contains(collections, target):
    return target in collections


# In[2]:

from time import time

# binary search
def bs_contains(ordered_lists, target):
    low = 0
    high = len(ordered_lists) - 1
    while low <= high:
        
        mid = (high + low)/2
        if target == ordered_lists[mid]:
            return True
        elif target < ordered_lists[mid]:
            high = mid - 1
        else: low = mid + 1
    return -(low+1)

def insertINplace(ordered, target):
    idx = bs_contains(ordered, target)
    if idx < 0:
        ordered.insert(-(idx+1), target)
        return
    ordered.insert(idx, target)
   
list1 = range(1, 10, 2)
print list1
print bs_contains(list1, 8)

list1


# In[6]:

class BinaryNode:
    def __init__(self, value=None):
        """Create binary node"""
        self.value = value
        self.left = None
        self.right = None
        
    def add(self, val):
        """Adds a new node to the tree containing this value"""
        if val <= self.value:
            if self.left: 
                ''' if left child created just add the value'''
                self.left.add(val)
            else:
                self.left = BinaryNode(val)
        else:
            if self.right:
                self.right.add(val)
            else:
                self.right = BinaryNode(val)
    
    def delete(self):
        """
         Remove value of self from BinaryTree. Works in conjunction with remove
         method in BinaryTree
        """
        
        if self.left == self.right == None:
            return None
        if self.left == None:
            return self.right
        if self.right is None:
            return self.left
        child = self.left
        grandchild = child.right
        if grandchild:
            while grandchild.right:
                child = grandchild
                grandchild = child.right
            self.value = grandchild.value
            child.right = grandchild.left
        else:
            self.value = child.value
            self.left = child.left
    
    def inorder(self):
        ''' inorder traversal of tree rooted at given node'''
        if self.left:
            for n in self.left.inorder():
                '''print left child '''
                yield n
        yield self.value
        '''print parent'''
        if self.right:
            for n in self.right.inorder():
                '''print right child '''
                yield n

class BinaryTree:
    def __init__(self):
        """ create an empty binary tree """
        self.root = None
    
    def add(self, value):
        """Insert value into proper location in Binary Tree"""
        if self.root is None:
            self.root = BinaryNode(value) 
        else:
            self.root.add(value)
    
    def contains(self, target):
        """Check whether BST contains target value"""
        node = self.root
        while node:
            if target == node.value:
                return True
            if target < node.value:
                node = node.left
            else:
                node = node.right
        return False
    
    def remove(self, value):
        ''' remove a value from tree'''
        if self.root:
            self.root = self.removefromparent(self.root, value)
            
    def removefromparent(self, parent, value):
        ''' remove a value from tree rooted at parent '''
        if parent is None:
            return None
        if value == parent.value:
            return parent.delete()
        elif value < parent.value:
            parent.left = self.removefromparent(parent.left, value)
        else:
            parent.right = self.removefromparent(parent.right, value)
        return parent
        
    def __iter__(self):
        """In order traversal of elements in the tree"""
        if self.root:
            return self.root.inorder()

bt = BinaryTree()
bt.add('a')
bt.add('c')
bt.add('d')        

for x in bt:
    print x
    
bt.remove('c')

for x in bt:
    print x


# In[7]:

def balancedBtree(orderedlist):
    bt = BinaryTree()
    addRange(bt, orderedlist, 0, len(orderedlist)-1)
    return bt
def addRange(bt, orderedlist, low, high):
    if low <= high:
        mid = (low + high)/2
        bt.add(orderedlist[mid])
        addRange(bt, orderedlist, low, mid-1)
        addRange(bt, orderedlist, mid+1, high)
x = range(10)
print x
bbt = balancedBtree(x)
for x in bbt:
    print x

