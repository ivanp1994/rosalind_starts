# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 14:43:26 2023

@author: ivanp
"""
import pandas as pd

filename = "rosalind_hamm.txt"

with open(filename) as _f:
    _one = list(_f.readline().rstrip())
    _two = list(_f.readline().rstrip())

data = pd.DataFrame([_one,_two]).T
diff = len(data[data[0]!=data[1]])
print(diff)




