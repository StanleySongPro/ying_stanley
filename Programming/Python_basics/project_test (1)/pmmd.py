# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 17:35:42 2019

@author: Zhou YingYing
"""
#
#import numpy as np
#import pandas as pd

class Yingying():        
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.c = self.a+self.b
        
    def get_sum(self):
        '''
            We can use this function/method for summation
        '''
        return self.a + self.b
    
    def get_diff(self):
        return self.a - self.b
    
    def get_multiply(self):
        return self.a*self.b
    
    def get_division(self):
        return self.a/self.b
    
if __name__ == '__main__':
    yingying1 = Yingying(10, 2)
    yingying2 = Yingying(100, 2)
    
    print('yingying1 sum: {}'.format(yingying1.get_sum()))
    print('yingying2 div: {}'.format(yingying2.get_division()))