#!/usr/bin/python3
# -*-coding:utf-8 -*-

from Bin import Bin
from Item import Item


goods = [3, 5, 3, 4, 2, 1]
num_item = len(goods)
capacity = 7
max_weight_sofar = 0
cur_loading = 0
cur_rest = capacity
path = []

def backtracking(cur_level):
	#	位于一个叶节点
	if cur_level > num_item:
		if cur_loading > max_weight_sofar:
			max_weight_sofar = cur_loading
			path_ = path[:]
		return path_
	#	不在一个叶节点，检查左子树
	if cur_loading+goods[cur_level-1]　<= capacity:
		cur_loading += goods[cur_level-1]
		path.append(goods[cur_level-1])
		backtracking(cur_level+1)
		cur_loading -= goods[cur_level-1]

	#	搜索右子树
	backtracking(cur_level+1)


def loading():
	bins = []
	j = 0
	while len(goods) != 0:
		eles = backtracking(1)
		bin_ = Bin()
		bins.append(bin_)
		for ele in eles:
			bin_.add(Item(ele))
			goods.remove(ele)
		path.clear()
		num_item = len(goods)
		j += 1

	for i in range(len(bins)):
		print(i+1, ":", bins[i])



if __name__ == "__main__":
	loading()