#!/usr/bin/python3
# -*- coding:utf-8 -*-
from Cur_link import CurLink

# 测试使用相邻适配法(NF)解决BPP

bin_size = 7
goods = [3, 5, 3, 4, 2, 1]
bins = CurLink()
leng = goods.__len__()
form = '物品%d(重量为%d)------->箱子%d(剩余容量%d)'


def fit_one(i_, last):
    global bins
    bins.flush()
    while not last.flag:
        last.flag = 1
        if last.value:
            rest = bin_size-(goods[i_]+last.value)
            if rest >= 0:
                print(form % (i_+1, goods[i_], last.index+1, rest))
                return last
            else:
                last = last.next
        else:
            last = last.next

    bins.add_element(goods[i_])
    last_ = bins.head
    print(form % (i_+1, goods[i_], last_.index+1, bin_size-goods[i_]))
    return last_


bins.add_element(goods[0])
stop_tag = bins.head.next
last_used = bins.head
print(form % (1, 3, 1, 7-3))


if __name__ == '__main__':
    result = [last_used,]
    for i in range(1, leng):
        tem = fit_one(i, result[-1])
        result.append(tem)