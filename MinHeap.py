#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 17:24:08 2019

@author: Nigel
"""

# Cracking the Coding Interview Chapter 4

# Python Min Heap Implementation
import heapq

H = [1,3,9,7,5]
# CREATE Heap
# heapify function converts a reg list to a heap. Smallest element
# gets pushed to the root position(index 0), but others are not sorted
## left->right order is enumering each element from left->right for each level
heapq.heapify(H)
# heap property maintained
print(H)

# INSERT element into Heap (at the rightmost position of lowest level)
# heappush function adds an element to the heap without altering.
# iff new element is the smallest, put it in index 0
#heapq.heappush(H,0)
heapq.heappush(H,8)
# heap property maintained
print(H)

# REMOVE root(smallest element) from Heap
heapq.heappop(H)
# heap property maintained
print(H)

# REPLACING root(smallest element)
# puts the replaced element at some place without fixing order, just
# maintaining the heap property
heapq.heapreplace(H,6)
# heap property maintained
print(H)