#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 17:23:54 2019

@author: Nigel
"""

# Cracking the Coding Interview Chapter 1

# Python Rabin-Karp Algorithm Implementation

# Rabin-Karp Hash Function
# hash(next substring) = (d* (hash(current substring)-current_1st_char*h) + new_char_fr_next_substring)mod(q)
# d : number of characters in alphabet
# q : a prime number
# m : length of pattern(substring)
# h : d^(m-1)

d = 256
# pat: pattern
# txt: text
def RabinKarpSearch(pat, txt, q):
    m = len(pat)
    n = len(txt)
    h = pow(d,m-1)
    
#    initial hash values 0 for empty strings
    pat_hash = hash("")
    txt_hash = hash("")
#    hash values are pre-computed from using the same hash functoin but 
#    starting from empty string and shifting m times.
    for i in range(m):
#        pattern's hash value
        pat_hash = (d*(pat_hash)+ord(pat[i]))%q
#        text's first substring window hash value
        txt_hash = (d*(txt_hash)+ord(txt[i]))%q
    
    for i in range(n-m+1):
#        first, compare hash values
        if pat_hash==txt_hash:
#            then compare actual characters
            if pat == txt[i:i+m]:
                print("Pattern found at index "+str(i))
        if i < n-m:
#            hash value update. remove leading digit and add trailing digit
            txt_hash = (d*(txt_hash-ord(txt[i])*h)+ord(txt[i+m]))%q
    
txt = "GEEKS FOR GEEKS"
pat = "GEEK"
q = 101
RabinKarpSearch(pat,txt,q)