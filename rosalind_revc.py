# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 13:57:49 2023

@author: ivanp
"""

filename = "rosalind_revc.txt"

with open(filename) as _f:
    line = _f.read()

rev = line.replace("A","t").replace("T","a").replace("G","c").replace("C","g").upper()[::-1]
print(rev)