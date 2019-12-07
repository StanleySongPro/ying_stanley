# -*- coding: utf-8 -*-
"""
Created on Thu May  2 17:51:33 2019

@author: Zhou YingYing
"""

class Peer():


    def __init__(self, money, price_money, price_bottle, price_cover):
        self.money = money
        self.price_money = price_money
        self.price_bottle = price_bottle
        self.price_cover = price_cover
        self.peer = self.money // self.price_money
        self.bottle = self.peer
        self.cover = self.bottle

    def __repr__(self):
        return f'number of drunk{self.peer}number of left bottle {self.bottle}number of cover {self.cover}'
    
    def bottle_to_peer(self):
        while self.bottle >= 2:
            add = self.bottle // 2
            self.peer += add
            self.bottle += add
            self.cover += add
            self.bottle -= 2 * add
    
    def cover_to_peer(self):
        while self.cover >= 4:
            add = self.cover // 4
            self.peer += add
            self.bottle += add
            self.cover += add
            self.cover -= 4 * add
    
if __name__ == 'main':
    peer = Peer(money=10, price_money=2, price_bottle=2, price_cover=4)
    while peer.bottle >= 2 or peer.cover >= 4:
        peer.bottle_to_peer()
        peer.cover_to_peer()
        
        print(peer)



