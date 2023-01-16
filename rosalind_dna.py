# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 13:57:49 2023

@author: ivanp
"""

filename = "rosalind_dna.txt"

with open(filename) as _f:
    line = _f.read()

x = ""
for nuc in ['A', 'C', 'G',  'T' ]:
    x = f"{x}{line.count(nuc)} "
print(x)