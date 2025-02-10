class TreeNode:
    def __init__(self, val=0 , left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BTree:
    def __init__(self, root=None):  # 默认root为空
        self.root = root

    def add(self, item):
        '''利用队列'''
        node = TreeNode(item)  #
        if not self.root:
            self.root = node
            return
        queue = list()
        queue.append(self.root)
        while queue:
            cur_node = queue.pop(0)  # 移除列表中第一个元素，相当于队列中最后一个。
            if not cur_node.left:
                cur_node.left = node
                return
            else:
                queue.append(cur_node.left)

            if not cur_node.right:
                cur_node.right = node
                return
            else:
                queue.append(cur_node.right)


    def bredath_travle(self):
        """层次遍历返回二维数组"""
        if not self.root:
            return []
        res = []
        queue = [self.root]
        while queue:
            res.append([node.val for node in queue])
            L = []  #存储当前层的孩子节点列表
            for node in queue:
                if node.left :  #如果左子节点存在，入队列
                    L.append(node.left)
                if node.right:    #如果右子节点存在，入队列
                    L.append(node.right)
            queue = L   #后把queue更新成下一层的结点，继续遍历下一层
        return res

    def levelOrderBottom(self):
        """自底向上的层序遍历"""
        if not self.root:
            return []
        res = []
        queue = [self.root]
        while queue:
            L = []
            res.append([node.val for node in queue])
            for node in queue:
                if node.left:
                    L.append(node.left)
                if node.right:
                    L.append(node.right)
            queue = L
        return res[::-1]


if __name__ == "__main__":
    tree = BTree()
    tree.add(0)
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)
    print(tree.bredath_travle())
    print(tree.levelOrderBottom())
