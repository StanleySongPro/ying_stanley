# -*- coding: utf-8 -*-
"""
Created on Thu May  9 15:03:06 2019

@author: Zhou YingYing
"""
"""
def solution(number):
    res = []
    for i in range(number):
        if i%3 ==0 or i%5==0:
            res.append(i)
       # b = list(set(res))
    print(res)
    #print(b)
    return sum(res)
print(solution(10))
"""
'''
def to_camel_case(text):
    #your code here
    for i in range(len(text)):
        if text[i] == '_':
            text[i+1].upper()
            text.split('_')
        elif text[i] == '-':
            text[i+1].upper()
            text.split('-')
    return text
print(to_camel_case('I_love_beijing'))
'''
'''
text='I_love_beijing'
for i in range(len(text)):
    if text[i] == "-":
        print(text[i])
        
    elif text[i] == "_":
        nes = text.replace(text[i+1],text[i+1].upper())
        nes1 = nes.replace(nes[i],'')
print(nes1)
'''
'''
def to_camel_case(text):
    #your code here
    for i in range(len(text)):
        if text[i] == '_' or text[i] == '-':
            t1 = text.replace(text[i+1],text[i+1].upper())
            t2 = t1.replace(t1[i],'')
        
    return t2
text='he_Pippi-Was_Omoshiroi'
print(to_camel_case(text))
'''
'''
def to_camel_case(text):
    text = text.replace('_', '')
    text = text.replace('-', '')
    return text

text='he_Pippi-Was_Omoshiroi'
print(to_camel_case(text))
'''
def to_camel_case(text):
    text = text.replace('_', '#')
    text = text.replace('-', '#')
    for i, item in enumerate(text):
        if item == '#':
            try:
                text = text[:i+1] + text[i+1:].capitalize()
            except:
                text = text[:i+1]
    text = text.replace('#', '')
    return text

text='he_Pippi-Was_Omoshiroi'
print(to_camel_case(text))

text='the_stealth_warrior'
print(to_camel_case(text))

def to_camel_case(text):
    if text == "":
        print('None')
    else:
        text = text.replace('_', '-')
        for i, item in enumerate(text):
            if item == '-' and i < len(text)-1:
                text = text[:i+1] + text[i+1:].capitalize()
            elif item == '-' and i == len(text)-1:
                text = text[:i+1]
        text = text.replace('-', '')
        return text

text='he_Pippi-Was_Omoshiroi'
print(to_camel_case(text))

text='the_stealth_warrior'
print(to_camel_case(text))

text=''
print(to_camel_case(text))
