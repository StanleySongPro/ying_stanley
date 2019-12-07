# -*- coding: utf-8 -*-
"""
Created on Wed May 15 14:28:58 2019

@author: Zhou YingYing
"""

def check(t4,t5):
    
    result=[]
    for i in range(len(t4)):
        if t4[i] == t5[i]:
            result.append('y')
        elif t4[i] != t5[i]:
            result.append('n')
    
    return result

t4 =['Large cap growth to capture late business cycle growth, and where large caps are more resilient to rising financing and wage costs. Underweight driven by higher valuations relative to other markets',
     'Slight underweight as economic activity is slowing meaningfully',
     'Slight overweight as economy is supported by corporate reforms, and equities at attractive valuations',
     'Slight overweight to China "A" as valuations are attractive and supported by earnings growth',
     'Earnings are expected to slow, though a weaker-stable USD may help to support equities in the region',
     'Focus on currency-hedged global government bonds to buffer portfolio volatility during periods of stress',
     'Maintaining no exposure as low incremental yield and long duration exposure are less attractive than other segments',
     'Maintain short duration which provides better yield to broad market with less sensitivity to interest rate changes',
     'One of the most attractive yields across major fixed income markets backed by policy support and sentiment',
     'Range-bound USD eases downward pressure on EMD which adds to portfolio diversification']
t5 = ['Large cap growth to capture late business cycle growth, and where large caps are more resilient to rising financing and wage costs. Underweight driven by higher valuations relative to other markets',
      'Slight underweight as economic activity is slowing meaningfully, and as valuations have trended up',
      'Slight overweight as economy is supported by corporate reforms, and equities at attractive valuations',
      'Slight overweight to China "A" as valuations are attractive and supported by earnings growth',
      'Weaker-stable USD may help to support equities in the region',
      'Focus on currency-hedged global government bonds to buffer portfolio volatility during periods of stress',
      'Maintaining no exposure as low incremental yield and long duration exposure are less attractive than other segments',
      'Maintain short duration which provides better yield to broad market with less sensitivity to interest rate changes',
      'One of the most attractive yields across major fixed income markets backed by policy support and sentiment',
      'Range-bound USD eases downward pressure on EMD which adds to portfolio diversification']

print(check(t4,t5))
