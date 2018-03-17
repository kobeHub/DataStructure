#!/usr/bin/python3
# -*-coding:utf-8 -*-

from Bin import Bin
from Item import Item

max_weight_sofar = 0
path = []
perfect = []
goods_ = []


def backtracking(cur_level, num_item, capacity, cur_loading=0):
	global max_weight_sofar, path
	#	位于一个叶节点
	if cur_level > num_item:
		global perfect 
		if cur_loading > max_weight_sofar:
			max_weight_sofar = cur_loading
			perfect = path[:]
			#print(id(perfect))
		#print(perfect)	
		path.clear()
		return
	#	不在一个叶节点，检查左子树
	elif cur_loading + goods_[cur_level-1] <= capacity:
		cur_loading += goods_[cur_level-1]
		path.append(goods_[cur_level-1])
		#print(cur_level, path)
		backtracking(cur_level+1, num_item, capacity, cur_loading)
		cur_loading -= goods_[cur_level-1]

	#	搜索右子树
	else:
		backtracking(cur_level+1, num_item, capacity, cur_loading)


def loading(goods, cap):
	global goods_
	goods_ = goods
	bins = []
	j = 0
	global max_weight_sofar
	while len(goods_):
		backtracking(1, len(goods_), capacity=cap)

		bin_ = Bin(cap)
		bins.append(bin_)
		#print(perfect, id(perfect))

		for ele in perfect:
			bin_.add(Item(ele))
			goods.remove(ele)
		
		path.clear()
		perfect.clear()
		num_item = len(goods)
		j += 1
		max_weight_sofar = 0

	for i in range(len(bins)):
		print(i+1, ":", bins[i])
	return bins



if __name__ == "__main__":
	goods = [3, 5, 3, 4, 2, 1, 4, 6, 2,3, 36, 56, 23]
	loading(goods, 87)