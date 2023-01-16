# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 14:12:11 2023

@author: ivanp
"""

filename = "rosalind_gc.txt"

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

gc_dic = dict()
for _fastid,_fastseq in read_fasta(filename).items():
    gc_dic[_fastid] = (_fastseq.count("G") + _fastseq.count("C"))/len(_fastseq)
    
gc_max = max(gc_dic,key=gc_dic.get)

print(f"{gc_max[1:]}\n{gc_dic[gc_max]*100:.5f}")
