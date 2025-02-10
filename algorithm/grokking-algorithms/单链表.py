class Node(object):
    """ 节点 """
    def __init__(self, elem):
        self.elem = elem
        self.next = None   # 一开始还不知道节点的next指向谁，所以先指向None


class SingleLinkList(object):
    """ 单链表 """
    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        """ 链表是否为空 """
        return self.__head == None

    def length(self):
        """ 链表长度 """
        # cur游标,用来遍历节点
        cur = self.__head
        # count记录数量
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count


    def travel(self):
        """遍历整个链表"""
        cur = self.__head
        while cur != None:
            print(cur.elem, end=" ")
            cur = cur.next

    def add(self,item):
        """链表头部添加元素，头插法"""
        node = Node(item)
        node.next = self.__head
        self.__head = node


    def append(self, item):
        """链表尾部添加元素,尾插法"""
        node = Node(item)
        if self.is_empty():
             self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node


    def insert(self, pos, item):
        """指定位置添加元素,pos从0开始"""
        if pos <= 0:
            self.add(item)
        elif pos > (self.length()-1):
            self.append(item)
        else:
            pre = self.__head
            count = 0
            while count < pos-1:
                # 当循环退出后，pre指向pos-1位置
                count += 1
                pre = pre.next

            node = Node(item)
            node.next =pre.next
            pre.next = node



    def remove(self, item):
        """删除节点"""
        cur = self.__head
        pre = None
        while cur != None:
            if cur.elem == item:
                # 先判断此节点是否是头节点
                if cur == self.__head:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next

    def search(self, item):
        """查找节点是否存在"""
        cur = self.__head
        while cur != None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
            return False



if __name__ == "__main__":
    ll = SingleLinkList()
    print(ll.is_empty())
    print(ll.length())
    ll.append(1)

    ll.append(6)
    print(ll.is_empty())
    print(ll.length())
    ll.append(2)
    ll.append(7)
    ll.append(9)
    ll.add(9)  # 9 1 6 2 7 9
    ll.insert(-1,12)  # 12 9 1 6 2 7 9
    ll.insert(20,18)  # 12 9 1 6 2 7 9 18
    ll.insert(2,20)  # 12 9 20 1 6 2 7 9 18
    ll.remove(12)
    ll.remove(18)
    ll.remove(20)   # 9 1 6 2 7 9
    ll.travel()

