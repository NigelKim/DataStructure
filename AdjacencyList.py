#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 20:54:13 2019

@author: Nigel
"""

# Cracking the Coding Interview Chapter 4

# Graph as Adjacency List
# Python Adjacency List Implementation

class Graph:
    
    def __init__(self):
        self.graph = []
        
    def addNode(self,node):
        self.graph.append(node)
        
    def PrintGraph(self):
        for node in self.graph:
            childrenString = ""
            for child in node.children:
                childrenString = childrenString+str(child)+" "
            print(str(node.name)+": "+childrenString)
        
class Node:
    
    def __init__(self, name):
        self.name = name
        self.children = None
        
    def child(self,childrenlist):
        self.children = childrenlist
        
g = Graph()

z = Node(0)
z.child([1])
g.addNode(z)

o = Node(1)
o.child([2])
g.addNode(o)

tw = Node(2)
tw.child([0,3])
g.addNode(tw)

thr = Node(3)
thr.child([2])
g.addNode(thr)

g.PrintGraph()