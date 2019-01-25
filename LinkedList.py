#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 14:18:28 2019

@author: Nigel
"""
# Cracking the Coding Interview Chapter 2

# Python Linked List Implementation
# In Linked List, no constant time access to index,
# but Allows Constant Time access to the head node

# create Node object first
class Node:
    def __init__(self, dataval=None):
#        declare and initialize member variables
        self.dataval = dataval
#        singly linked... therefore only nextval pointer is created
        self.nextval = None

# create Singly Linked List object
class SLinkedList:
    def __init__(self):
        self.headval = None

# main
        
# construct empty singly linked list
list1 = SLinkedList()
# initialize HEAD node value
list1.headval = Node("Monday")
e2 = Node("Tuesday")
e3 = Node("Wednesday")


# list1.headval is a NODE object.
# we can call the nextval pointer from the NODE object
(list1.headval).nextval = e2
e2.nextval = e3

# check - SUCCESSFUL
pointer = list1.headval
while pointer != None:
    print(pointer.dataval)
    pointer = pointer.nextval