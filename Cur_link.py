class Node:
    def __init__(self, val, nt=None, ins=0, fla=0):
        self.value = val
        self.next = nt
        self.index = ins
        self.flag = fla     # 用于表示是否监测过该节点

    def __str__(self):
        return str(self.value)

    # 循环链表实现


class CurLink:
    def __init__(self):
        self.headNode = Node(None, None, 0)
        self.headNode.next = self.headNode
        self.head = self.headNode
        self.size = 0

    def __str__(self):
        if self.size == 0:
            return 'empty'
        s = ''
        fin = self.head.next.next   # 头结点下一个节点为空，必须从下下个开始
        while fin.value:
            s += str(fin.value)
            if fin.next.value:
                s += ','
            fin = fin.next
        #   tem = s.split(',')[::-1]    # 使之恢复原来顺序
        return s

    def add_element(self, value):
        element_node = Node(value, None)
        if self.head.value is None:   # 和ｎｏｎｅ的比较需要用ｉｓ
            element_node.next = self.headNode
            self.head.next = element_node
            self.head = element_node
            self.size += 1
        else:
            element_node.index = self.size
            element_node.next = self.headNode
            self.head.next = element_node
            self.head = element_node
            self.size += 1

    def search(self, index):
        if self.size == 0:
            return 'empty'
        if index > self.size:
            return 'out of index'
        i = 0
        se = self.head.next
        while i <= self.size:
            if i == index:
                break
            se = se.next
            i += 1
        return se.next

    def delete(self, data):
        if self.size == 0:
            return 'empty'
        de = self.head
        cur = self.head.next
        while cur != self.head:
            if cur.value == data:
                break
            de = cur
            cur = cur.next
        if cur == self.head:
            return
        de.next = cur.next
        self.size -= 1

    def last_node(self):
       return self.head;


    def pre_node(self, node):
        return self.search(node.index-1)

    def flush(self):
        tem = self.head
        for i in range(self.size+1):
            tem.flag = 0
            i += 1
            tem = tem.next


if __name__ == "__main__":
    x = CurLink()
    x.add_element(65)
    print(x.search(0), x.head)
    x.add_element(58)

    x.add_element('df')
    print(x)
    print(x.head, x.head.next, x.head.next.next)
    print(x.head.index, x.head.next.index)

