#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 15:54:27 2019

@author: Nigel
"""

# Cracking the Coding Interview Chapter 4

# Python Binary Tree Implementation
# classes: Node, Tree

# create Root Node
class Node:
    def __init__(self,dataval):
        self.dataval = dataval
        self.left = None
        self.right = None
    
    def insert(self, dataval):
#        check current node is assigned a val
        if self.dataval:
#            if new is smaller, left
            if self.dataval > dataval:
#                if node doesn't exist, create node
                if self.left is None:
                    self.left = Node(dataval)
#                if node exists, recursively go to the far left
                else:
                    self.left.insert(dataval)
#            if new is larger, right
            elif self.dataval < dataval:
                if self.right is None:
                    self.right = Node(dataval)
                else:
                    self.right.insert(dataval)
#        else, assign a val
        else:
            self.dataval = dataval
        
    def PrintTree(self):
#        if left node exists
        if self.left:
            self.left.PrintTree()
        print(self.dataval)
        if self.right:
            self.right.PrintTree()
    
    def InOrderTraversal(self,root):
#        Left -> Root -> Right
        temp = []
        if root:
            temp = self.InOrderTraversal(root.left)
            temp.append(root.dataval)
            temp = temp + self.InOrderTraversal(root.right)
        return temp
    
    def PreOrderTraversal(self,root):
#        Root -> Left -> Right
        temp = []
        if root:
            temp.append(root.dataval)
            temp = temp + self.PreOrderTraversal(root.left)
            temp = temp + self.PreOrderTraversal(root.right)
        return temp
            
    def PostOrderTraversal(self,root):
#        Left -> Right -> Root
        temp = []
        if root:
            temp = self.PostOrderTraversal(root.left)
            temp = temp + self.PostOrderTraversal(root.right)
            temp.append(root.dataval)
        return temp
                    
class Tree:
    def __init__(self,root):
        self.root = root

    def insert(self, dataval):
        self.root.insert(dataval)
        
    def PrintTree(self):
        self.root.PrintTree()
   
#    def InOrderTraversal(self):
#        self.root.InOrderTraversal(self.root)
    
    
    

# initialize root node
rt = Node(12)
# create tree
t = Tree(rt)
t.insert(6)
t.insert(7)
t.insert(14)
t.insert(3)
t.insert(13)
#t.PrintTree()
inorder = rt.InOrderTraversal(rt)
preorder = rt.PreOrderTraversal(rt)
postorder = rt.PostOrderTraversal(rt)

print(inorder,"\n",preorder,"\n",postorder)
