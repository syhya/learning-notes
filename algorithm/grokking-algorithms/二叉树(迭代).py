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
        """层次遍历:队列"""
        if not self.root:
            return []
        res = []
        queue = []
        queue.append(self.root)
        while queue:
            cur_node = queue.pop(0)
            res.append(cur_node.val)
            if cur_node.left :
                queue.append(cur_node.left)
            if cur_node.right:
                queue.append(cur_node.right)
        return res

    def maxDepth(self, root):
        """二叉树的最大深度"""
        if not root:
            return 0
        return 1+max(self.maxDepth(root.left), self.maxDepth(root.right))

    def minDepth(self, root):
        """二叉树的最小深度"""
        '''
        1.没有根节点，那结果就是0
        2.有根节点，没有左右子树，结果为1
        3.没有左子树，有右子树。把右子树看成一棵新的树。
        4.没有右子树，有左子树。把左子树看成一棵新的树。
        5.既有左子树，又有右子树。那就把左右子树分别都看成新的树，最后比较谁的最近叶子的路径短，就取哪边。
        '''

        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        if not root.left:
            return 1+self.minDepth(root.right)
        if not root.right:
            return 1+self.minDepth(root.left)
        return 1+min(self.minDepth(root.left), self.minDepth(root.right))


    def preorder(self, root):
        '''先序遍历'''
        stack = [root]
        res = []
        while stack:
            s = stack.pop()
            if s:
                res.append(s.val)
                stack.append(s.right)   # 栈是后进先出，所以先right，后left.
                stack.append(s.left)
        return res

    def inorder(self, root):
        """中序遍历"""
        res = []
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            res.append(root.val)
            root = root.right
        return res


    def posorder(self, root):
        "后续遍历"
        stack = []
        res = []
        while stack or root:
            while root:  # 下行循环，直到找到第一个叶子节点
                stack.append(root)
                if root.left:   # 能左就左，不能左就右
                    root = root.left
                else:
                    root = root.right
            s = stack.pop()
            res.append(s.val)
            # 如果当前节点是上一节点的左子节点，则遍历右子节点
            if stack and s == stack[-1].left:
                root = stack[-1].right
            else:
                root = None
        return res

    #  二叉树的所有路径



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
    print("最大深度为%d" % tree.maxDepth(tree.root))
    print("最小深度为%d" % tree.minDepth(tree.root))
    print(tree.preorder(tree.root))
    print(tree.inorder(tree.root))
    print(tree.posorder(tree.root))
