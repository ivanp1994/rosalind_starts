# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 14:12:11 2023

@author: ivanp
"""
import pandas as pd
filename = "rosalind_cons.txt"

def read_fasta(filename):
    
    dic = dict()
    with open(filename,"r") as _f:
        line = _f.readline().rstrip()
        key = line
        value = ""
        while line:
            line = _f.readline().rstrip()
            if line.startswith(">"):
                dic[key]=value
                key = line
                value = ""
            else:
                value = value + line
        else:
            dic[key]=value
    return dic

def count_nucs(row,cols):    
    cross  = "".join(row.values)
    return (cross.count(cols[0]),cross.count(cols[1]),cross.count(cols[2]),cross.count(cols[3]))

dic_fasta = read_fasta(filename)
#split every element into a list
dic_fasta = {k:list(v) for k,v in dic_fasta.items()}

#create a daframe and consensus matrix
df = pd.DataFrame(dic_fasta)
_columns = ["A","T","C","G"]
con_mat = df.apply(count_nucs,axis=1,result_type="expand",cols=_columns)
con_mat.columns = _columns

#find the consensus - the largest element
cons = "".join(con_mat.idxmax(axis=1))

#print out the matrix
con_mat = con_mat.T
print(cons)
for _,row in con_mat.iterrows():
    values = " ".join(row.astype(str))
    print(f"{row.name}: {values}")