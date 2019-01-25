#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 19:23:56 2019

@author: Nigel
"""

# Cracking the Coding Interview Chapter 4

# Python Topological Sort Implementation
import collections
class Graph:
    def __init__(self,num_v):
        self.gdict = collections.defaultdict(set)
        self.V = num_v
    
    def addNode(self,v,adj):
#        v is self node. adj is a set of adjacent nodes
        self.gdict[v] = adj
    
    def addEdge(self,v,new_v):
        self.gdict[v].add(new_v)
        
    def TopologicalSort(self):
        visited = [False]*self.V #repetition. list of booleans for vertices
        stack = collections.deque()
        
        for i in range(self.V): #iterating thru vertices
            if visited[i] == False:
                self.TShelper(i,visited,stack)
        print(stack)
        
    def TShelper(self,v,visited,stack):
#        mark current vertex as visited
        visited[v] = True
        for i in self.gdict[v]:
            if visited[i] == False:
#                recursive call to search deeper into the node.
                self.TShelper(i,visited,stack)
#        recursive call makes the stack to have the most outgoing adf vertex
#        pushed first, and startnode last
        stack.appendleft(v)

g = Graph(6) 
g.addEdge(5, 2); 
g.addEdge(5, 0); 
g.addEdge(4, 0); 
g.addEdge(4, 1); 
g.addEdge(2, 3); 
g.addEdge(3, 1);
g.TopologicalSort()