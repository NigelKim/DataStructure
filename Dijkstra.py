#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 20:29:15 2019

@author: Nigel
"""

# Cracking the Coding Interview Chapter 4

# Python Dijkstra's Algorithm Implementation

import collections
class Graph:
    def __init__(self):
        self.gdict = collections.defaultdict(list) # adjacent vertex dictionary
        self.numV = 1 # number of vertices
        self.sptDict = {} # shortest path tree dictionary
        self.dist = [] # list of remaining vertices' distances from startnode
        self.vSet = [] # list of remaining vertices in the graph
    
    def addEdge(self,v,new_v,weight):
#        append new edge to the neighbor dictionary in tuple (destination, weight)
        self.gdict[v].append((new_v,weight))
        
        if v not in self.vSet:
            self.vSet.append(v)
            self.numV += 1
            self.dist += [float('Inf')]
        if new_v not in self.vSet:
            self.vSet.append(new_v)
            self.numV += 1
            self.dist += [float('Inf')]
#        initializing the graph's self.dist list as [0 inf inf inf ...]
        self.dist[0] = 0
    
    def Dijkstra(self,startnode):

        while len(self.vSet)!=0:
            #   at startvertex
            if self.dist[0] == 0:
                v = startnode
            #   if not at startvertex
            else:
                #   unvisited vertex with the shortest distance is selected as new v
                v = self.vSet[self.dist.index(min(self.dist))]
            if v not in self.sptDict:
                #   add startvertex in sptDict dictionary
                if self.dist[0] == 0:
                    my_dist = 0
                    self.sptDict[v] = my_dist
                #   add new vertex and its shortest path in sptDict
                else:
                    my_dist = min(self.dist)
                    self.sptDict[v] = my_dist
            
            for edge in self.gdict[v]:
                # check adjacent vertices and update distance list
                if self.dist[self.vSet.index(edge[0])]> my_dist+edge[1]:
                    self.dist[self.vSet.index(edge[0])]=my_dist+edge[1]
            
            # Remove the vertex that is determined
            self.vSet.remove(v)
            self.dist.remove(my_dist)

        print("Shortest Path Tree from startnode ",startnode," (destination: total weight): ",g.sptDict)

g = Graph()
g.addEdge(0,1,4)
g.addEdge(0,7,8)
g.addEdge(1,2,8)
g.addEdge(1,7,11)
g.addEdge(7,8,7)
g.addEdge(7,6,1)
g.addEdge(2,8,2)
g.addEdge(6,8,6)
print("nodes in graph: ",g.vSet)
#print(g.gdict)
#print(g.dist)
g.Dijkstra(0)
    