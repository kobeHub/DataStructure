#!/usr/bin/python3
# -*-oding:utf-8 -*-

from Cur_link import CurLink

# 定义物品类
class Item:
    
    def __init__(self, size):
        self.size = size

    def __str__(self):
        return "Size : "+str(self.size)

    def __repr__(self):
        return str(self.size)

    def __cmp__(self,other):
        return cmp(self.size,other.size)

    # 两个物品的相加
    def __add__(self,other):
        return Item(self.size + other.size)

    def __radd__(self, other):
    	return Item(self.size + other)

def bin_factory(num_bins, capacity=1):
    bins = []
    for i in range(num_bins):
        bins.append(Bin(capacity))

    return bins;

def clean_bins(bins):
    for b in bins:
        b.clean()


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
    		


record = 0
def new_bin(cap_):
	global record
	record = +1
	return Bin(cap_), record


################## Generator ####################

def nf_binpick(items, cap):

	num = len(items)
	bins = []
	for i in range(num):
		bins.append(Bin(cap))
		i += 1
	form = "第%d个物品（重量为：%d）------->第%d个箱子（剩余容量：%f）"

	for index in range(num):
		for ji in range(num):
			if (items[index] <= bins[ji].remaining):
				if bins[ji].add(Item(items[index])):
					print(form % (index+1, items[index], ji+1, bins[ji].remaining))
				break
		
	for i in range(num):
		if bins[i].empty():
			bins[i] = None
	for i in range(bins.count(None)):
		bins.remove(None)
	return bins




if __name__ == "__main__":
    list = [3, 5, 3, 4, 2, 1]
    bins = nf_binpick(list, 7)
    for i in range(len(bins)):
    	print(i+1, ":", bins[i])
