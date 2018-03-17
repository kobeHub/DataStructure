#!/usr/bin/python3
# -*-coding:utf-8 -*-

from live_node_queue import live_queue
from Bin import Bin
from Item import Item

#	用于存储活动节点的全局变量
live_queue = live_queue()
max_weight_sofar = 0
path = []
perfect = []



#	将相应权值的节点加到活动队列中
def add_live_node(cur_weight, num_item, num_level):
	
	if num_item == num_level:
	#	到达叶节点
		global max_weight_sofar
		if cur_weight > max_weight_sofar:
			max_weight_sofar = cur_weight
			
	else:
		live_queue.push(cur_weight)


def brand_and_branch(goods, capacity):
	#	作为曾结束的标志
	live_queue.push(-1)
	#	初始化第一层的Ｅ－节点
	e_node_level = 1
	max_weight_sofar = 0
	e_node_weight = 0	#当前已加载的重量
	num_item = len(goods)
	global path

	while 1: 
	#　检查左孩子
		if e_node_weight+goods[e_node_level-1] <= capacity:
			add_live_node(e_node_weight+goods[e_node_level-1], num_item, e_node_level)
			path.append(goods[e_node_level-1])
	#	检查右孩子
		else:
			add_live_node(e_node_weight, num_item, e_node_level)

	#	取得下一个Ｅ－节点
		e_node_weight = live_queue.pop()

		if e_node_weight == -1:
			global perfect
		#层结束，找到下一个Ｅ－节点
			if(live_queue.empty()):
				perfect = path[:]
				#print(id(perfect))
				path.clear()
				return 
			live_queue.push(-1)
			e_node_weight = live_queue.front()
			live_queue.pop()
			e_node_level += 1
		


def loading_(goods, cap):
	bins = []
	j = 0
	global max_weight_sofar, path
	
	while len(goods):
		brand_and_branch(goods, cap)

		bin_ = Bin(cap)
		bins.append(bin_)
		#print(perfect, id(perfect))

		for ele in perfect:
			bin_.add(Item(ele))
			goods.remove(ele)
		
		
		perfect.clear()
		num_item = len(goods)
		j += 1
		
	for i in range(len(bins)):
		print(i+1, ":", bins[i])
	return bins


if __name__ == "__main__":
	goods = [3, 5, 3, 4, 2, 1,56, 67, 12]
	loading_(goods, 87)
