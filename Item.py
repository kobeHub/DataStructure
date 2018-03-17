#!/usr/bin/python3
# -*-coding:utf-8 -*-
# 定义物品类
class Item:
    
    def __init__(self, size):
        self.size = size

    def __str__(self):
        return str(self.size)

    def __repr__(self):
        return str(self.size)

    def __cmp__(self,other):
        return cmp(self.size,other.size)

    # 两个物品的相加
    def __add__(self,other):
        return Item(self.size + other.size)
    # 用于整数和物品的相加
    def __radd__(self, other):
    	return Item(self.size + other)


def clean_bins(bins):
    for b in bins:
        b.clean()
