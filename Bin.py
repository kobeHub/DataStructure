#!/usr/bin/python3
# -*-coding:utf-8 -*-

from Item import Item
#	定义箱子类
class Bin:
    def __init__(self, capacity=1):
        self.capacity = capacity
        self.remaining = capacity
        self.items = []

    def __str__(self):
        strn = "已使用 : "+str(self.capacity-self.remaining)
        strn += "\t   装入的物品 : "+str(self.items)
        strn += "\t   (总重量为： "
        if sum(self.items):
            strn += str(sum(self.items).size)
        else:
            strn += "0"
        strn += "\t 容量："+str(self.capacity)+")"
        return strn

    def __repr__(self):
        return str(self.used())

    def __cmp__(self, other):
        return cmp(other.remaining, self.remaining)

    def add(self, item):
        if (not isinstance(item, Item)) or (item.size > self.remaining):
            return False
        self.remaining -= item.size
        self.items.append(item)
        return True

    def force_add(self, item):
        self.remaining -= item.size
        self.items.append(item)

    def rem_last(self):
        if not self.items:
            return False
        self.remaining += self.items.pop().size
        return True

    def used(self):
        return self.capacity-self.remaining

    def clean(self):
        self.remaining = self.capacity
        self.items = []

    def empty(self):
    	  return self.remaining == self.capacity
