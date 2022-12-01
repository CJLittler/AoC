# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 17:54:32 2022

@author: cjlit
"""
import os
os.chdir('C:/Users/cjlit/OneDrive/Documents/AOC/2022/')
filepath = 'inputs/day1.txt'
f = open(filepath)
day1dat = f.readlines()
f.close()
def day1func(dat):
    maxv = [0,0,0]
    current = 0
    for i in dat:
        if(i == "\n"):
            current = 0
        else:
            n = int(i.replace("\n", ""))
            current += n
            if current > maxv[0]:
                maxv[0] = current
            elif current > maxv[1]:
                maxv[1] = current
            elif current > maxv[2]:
                maxv[2] = current
    return(maxv)
        