#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 18:47:23 2019

@author: Nigel
"""

# Cracking the Coding Interview Chapter 4

# Python DFS & BFS Implementation

class Graph:
    def __init__(self):
        self.gdict = {}
    
    def addNode(self,v,adj):
#        v is self node. adj is a set of adjacent nodes
        self.gdict[v] = adj
        
# Depth First Search (DFS) 
# Uses recursion and visit marker
def DFS(graph, start, visited = None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    for next in graph[start]-visited:
        DFS(graph, next, visited)
    return visited

# Breadth First Search (BFS)
# Uses QUEUE
# in 'collections library' and use 'deque' for general stack or queue implementation
    # deque means double-ended queue
import collections
def BFS(graph, startnode):
    seen = {startnode}
    queue = collections.deque([startnode])
    while queue: # while queue isn't empty
        vertex = queue.popleft()
        print(vertex)
        for node in graph[vertex]:
            if node not in seen:
                seen.add(node)
                queue.append(node)

g = Graph()
g.addNode("a",{'b','c'})
g.addNode("b",{"a","d"})
g.addNode("c",{"a","d"})
g.addNode("d",{"e"})
g.addNode("e",{"a"})
#print(g.gdict)
DFS(g.gdict, "a")
print('\n')
BFS(g.gdict, "a")