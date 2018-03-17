# -*-coding=utf-8-*-

class live_queue:
    def __init__(self):
        self.items = []

    def empty(self):
        return self.items == []

    def push(self,item):
        ''''
        时间复杂度为 O(n)
        '''
        self.items.insert(0,item)

    def pop(self):
        '''
        时间复杂度为O(1)
        '''
        return self.items.pop()

    def size(self):
        return len(self.items)


    def front(self):
        return int(self.items[-1])

    def __str__(self):
        return str(self.items)

