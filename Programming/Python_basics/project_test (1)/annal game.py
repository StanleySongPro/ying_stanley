# -*- coding: utf-8 -*-
"""
Created on Fri May  3 18:16:57 2019

@author: Zhou YingYing
"""

score = [0]
import random
u = 0
for u in range(0,1000):
    if sum(score) < 2019:
        i = random.randint(1,11)
        score.append(i)
        u = u+1
    elif sum(score) == 2019:     
        print(u)

print(sum(score))   
print(u)