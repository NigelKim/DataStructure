#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 15:08:27 2019

@author: Nigel
"""

# Cracking the Coding Interview Chapter 3

# Python QUEUE Implementation (FIFO)
# In QUEUE, no constant time access to index,
# but Allows Constant Time add/remove

class Queue:
    def __init__(self):
        self.queue = []
    
    def add(self, dataval):
        if dataval not in self.queue:
            self.queue.insert(0,dataval)
            return True
        else:
            return False
    
    def remove(self):
        if len(self.queue) <= 0:
            return ("No element in the Queue")
        else:
            return self.queue.pop()
    
    def peek(self):
        if len(self.queue) <= 0:
            return ("No element in the Queue")
        else:
            return self.queue[-1]
    
    def isEmpty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False
        
q = Queue()
q.add("Mon")
q.add("Tues")
q.add("Wed")
print(q.peek())
print(q.remove())
print(q.remove())
print(q.isEmpty())

print(q.remove())
print(q.isEmpty())