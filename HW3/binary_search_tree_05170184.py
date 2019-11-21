#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    def insert(self, root, val):
        if self.val == val:
            self.left = Node(x)
        elif self.val:
            if x < self.val:
                if self.left is None:
                    self.left = Node(x)
                else:
                    self.left.insert(x)
            elif x > self.val:
                if self.right is None:
                    self.right = Node(x)
                else:
                    self.right.insert(x)
        else:
            self.val = x
            root = self
        return root
    def delete(self, root, target):
        if not root:
        return root
   # 將節點放入左邊的子結點，如果key value小於root value
        if root.val > target:
        root.left = delete_Node(root.left, target)
    # 將節點放入右邊的子結點，如果key value大於root value,
     elif root.val < target:
        root.right= delete_Node(root.right, target)
      # 刪除節點，如果root.value == key
        else:
        if not root.right:
        return root.left
        if not root.left:
            return root.right
        temp_val = root.right
        mini_val = temp_val.val
        while temp_val.left:
            temp_val = temp_val.left
            mini_val = temp_val.val
        # 將右邊子結點最小的結點刪除
        root.right = deleteNode(root.right,mini_val)
        return root
    def search(self, root, target):
        if target is None:
            root = self
            return root
        if target < self.val:
            if self.left is None:
                print('cannot search()')
            return self.left.search(target)
        elif target > self.val:
            if self.right is None:
                print('cannot search()')
            return self.right.search(target)
        else:
            print('cannot search()')
            root = self
            return root
    def replaceNodeData(self,key,value):
        self.val = key
        self.payload = value
    def modify(self, root, target, new_val):
        if target is None:
            root = self
            return root
        root = self.replaceNodeData(new_val, root, target)
        return root
        """
        :type root: TreeNode
        :type target: int
        :type new_val: int
        :rtype:TreeNode(the root of new completed binary search tree) (cannot search())
        """

