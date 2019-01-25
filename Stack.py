#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 14:55:23 2019

@author: Nigel
"""

# Cracking the Coding Interview Chapter 3

# Python Stack Implementation (LIFO)
# In Stack, no constant time access to index,
# but Allows Constant Time add/remove to the top

class Stack:
#    stack initial construction
#    with empty list
    def __init__(self):
        self.stack= []
    
    def push(self, dataval):
        if dataval not in self.stack:
#            list append method to implement PUSH
            self.stack.append(dataval)
            return True
        else:
            return False
    
    def pop(self):
        if len(self.stack) <= 0:
            return ("No element in the Stack")
        else:
            return self.stack.pop()
    
    def peek(self):
        if len(self.stack) <= 0:
            return ("No element in the Stack")
        else:
            return self.stack[-1]
    
    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

s = Stack()
s.push("Mon")
s.push("Tues")
s.push("Wed")
print(s.peek())
print(s.pop())
print(s.pop())
print(s.isEmpty())

print(s.pop())
print(s.isEmpty())