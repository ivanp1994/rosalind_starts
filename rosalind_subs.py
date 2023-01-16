# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 14:43:26 2023

@author: ivanp
"""
filename = "rosalind_subs.txt"

with open(filename) as _f:
    big = _f.readline().rstrip()
    small = _f.readline().rstrip()

occs = ""

for i in range(len(big)-len(small)+1):
    t = big[i:i+len(small)]
    if t==small:
        occs = f"{occs}{i+1} "

print(occs)
