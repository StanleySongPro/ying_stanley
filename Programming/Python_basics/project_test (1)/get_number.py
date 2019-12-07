# -*- coding: utf-8 -*-
"""
Created on Fri May  3 14:21:23 2019

@author: Zhou YingYing
"""
    
    
# =============================================================================
# def is_prime(n):
#     '''add prime numbers in a list called primelst'''
#     if n == 1:
#         
# =============================================================================
        
primes = []
composite = []
for possiblePrime in range(6598730000, 6598739999):
    
    # Assume number is prime until shown it is not. 
    isPrime = True
    for num in range(2, possiblePrime):
        if possiblePrime % num == 0:
            isPrime = False
      
    if isPrime:
        primes.append(possiblePrime)
    else:
        composite.append(possiblePrime)
# =============================================================================
# print(primes)
# print(composite)
# 
# =============================================================================
res_lst = []
for p in primes:
    for q in primes:
        for z in composite:
            if p*q == z:
                res_lst.append(z)
                res = list(dict.fromkeys(res_lst))
                print(res[60])
            
            