# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 17:40:56 2019

@author: Zhou YingYing
"""

from pmmd import Yingying

yingying1 = Yingying(10, 2)
yingying2 = Yingying(100, 2)

print('yingying1 diff: {}'.format(yingying1.get_diff()))
print('yingying2 multiply: {}'.format(yingying2.get_multiply()))