# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 13:57:49 2023

@author: ivanp
"""

filename = "rosalind_rna.txt"

with open(filename) as _f:
    line = _f.read()

rna = line.replace("T","U")
print(rna)