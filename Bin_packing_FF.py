#!/usr/bin/python3
# -*- coding:utf-8 -*-

from Bin import Bin
from Item import Item

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



"""
if __name__ == "__main__":
    list = [3,5,3,4,2,1,56,67,12]
    bins = nf_binpick(list, 87)
    for i in range(len(bins)):
    	print(i+1, ":", bins[i])
"""

