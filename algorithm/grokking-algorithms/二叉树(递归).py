class Node(object):

    def __init__(self, item):
        self.elem = item
        self.lchild = None
        self.rchild = None

class Tree(object):
    '''  二叉树  '''
    def __init__(self):
        self.root = None

    def add(self, item):
        node = Node(item)
        if self.root is None:
            self.root = node
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            if cur_node.lchild is None:
                cur_node.lchild = node
                return
            else:
                queue.append(cur_node.lchild)

            if cur_node.rchild is None:
                cur_node.rchild = node
                return
            else:
                queue.append(cur_node.rchild)

    def breadth_travel(self):
        """广度优先遍历(层次遍历) """
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.elem, end = " ")
            if cur_node.lchild is not None:
                queue.append(cur_node.lchild)
            if cur_node.rchild is not None:
                queue.append(cur_node.rchild)

    # 重要： 使用递归
    def preorder(self, node):
        ''' 先序遍历:根左右 '''

        if node is None:
            return
        print(node.elem, end =" ")
        self.preorder(node.lchild)
        self.preorder(node.rchild)

    def inorder(self, node):
        ''' 中序遍历:左根右 '''

        if node is None:
            return
        self.inorder(node.lchild)
        print(node.elem, end=" ")
        self.inorder(node.rchild)

    def backorder(self, node):
        ''' 后序遍历:左右根 '''

        if node is None:
            return
        self.backorder(node.lchild)
        self.backorder(node.rchild)
        print(node.elem, end=" ")

    def maxDepth(self, node):
        '''二叉树的最大深度'''
        if not node :
            return 0
        return 1+max(self.maxDepth(node.lchild), self.maxDepth(node.lchild))

    def minDepth(self, node):
        ''' 二叉树的最小深度'''
        if not node:
            return 0
        if not node.lchild and not node.rchild:
            return 1
        if not node.rchild:
            return 1+self.minDepth(node.lchild)
        if not node.lchild:
            return 1+self.minDepth(node.rchild)
        return 1+min(self.minDepth(node.lchild), self.minDepth(node.rchild))



if __name__ == "__main__":
    tree = Tree()
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
    tree.breadth_travel()
    print(" ")
    tree.preorder(tree.root)
    print(" ")
    tree.inorder(tree.root)
    print(" ")
    tree.backorder(tree.root)
    print(" ")
    print(tree.root)
    print("最大深度为%d" % tree.maxDepth(tree.root))
    print("最小深度为%d" % tree.minDepth(tree.root))



