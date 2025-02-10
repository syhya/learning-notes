class BiTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

class BST:
    def __init__(self, li = None):
        self.root = None
        if li:
            for val in li:
                self.insert_no_rec(val)   # 调用迭代插入

    # 递归插入
    def insert(self, node, val):
        if not node:
            node = BiTreeNode(val)
        elif val < node.data:
            node.left = self.insert(node.left, val)
            node.left.parent = node
        elif val > node.data:
            node.right = self.insert(node.right, val)
            node.right.parent = node
        return node


    # 迭代写法
    def insert_no_rec(self, val):
        p = self.root
        if not p:    # 空树
            self.root = BiTreeNode(val)
            return
        while p:
            if val < p.data:
                if p.left:
                    p = p.left
                else:    # 左孩子不存在
                    p.left = BiTreeNode(val)
                    p.left.parent = p
                    return
            elif val > p.data:
                if p.right:
                    p = p.right
                else:
                    p.right = BiTreeNode(val)
                    p.right.parent = p
                    return
            else:
                return

                # 中序
    def in_order(self, root):
        if not root:
            return
        self.in_order(root.left)
        print(root.data, end=" ")
        self.in_order(root.right)


    def query(self, node, val):
        if not node:
            return None
        if node.data < val:
            return self.query(node.right, val)
        elif node.data > val:
            return self.query(node.left, val)
        else:
            return node

    def query_no_rec(self, val):
        p = self.root
        while p:
            if p.data < val:
                p = p.right
            elif p.data > val:
                p = p.left
            else:
                return p
        return None

    def remove_node1(self, node):
        # 情况1：node 是叶子节点
        if not node.parent:
            self.root = None
            # node是它父亲的左孩子
        if node == node.parent.left:
            node.parent.left = None

        else:  # 右孩子
            node.parent.right = None

    def remove_node2(self, node):
        # 情况2:node只有一个左孩子
        if not node.parent: # 根节点
            self.root = node.left
            node.left.parent = None
        elif node == node.parent.left:
            node.parent.left = node.left
            node.left.parent = node.parent
        else:
            node.parent.right = node.left
            node.left.parent = node.parent

    def remove_node3(self, node):
        # 情况3:node只有一个右孩子
        if not node.parent:
            self.root = node.right
        elif node == node.parent.right:
            node.parent.left = node.right
            node.right.parent = node.parent
        else:
            node.parent.right = node.right
            node.right.parent = node.parent

    def delete(self, val):
        if self.root:  # 不是空树
            node = self.query_no_rec(val)
            if not node: # 不存在
                return False
            if not node.left and not node.right:  #1.叶子节点
                self.remove_node1(node)
            elif not node.right:  # 2.只有一个左孩子
                self.remove_node2(node)
            elif not node.left: # 3.只有一个右孩子
                self.remove_node3(node)
            else: # 4.两个孩子都有
                min_node = node.right
                while min_node.left:
                    min_node = min_node.left
                node.data = min_node.data
                # 删除min_node
                if min_node.right:
                    self.remove_node3(min_node)
                else:
                    self.remove_node1(min_node)


import random
li = list(range(0, 300, 2))
random.shuffle(li)
tree = BST(li)
tree.in_order(tree.root)
print("")

print(tree.query_no_rec(4))
print(tree.query_no_rec(4).data)
print(tree.query_no_rec(3))


print("")
tree.delete(2)
tree.delete(0)
tree.delete(298)
tree.in_order(tree.root)







