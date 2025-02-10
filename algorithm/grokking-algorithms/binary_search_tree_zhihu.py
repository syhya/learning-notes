class TreeNode:
    def __init__(self, val):
        '''二叉搜索树节点的定义'''
        self.val = val
        self.left = None
        self.right = None

    # 递归来插入
    def insert(self, root, val):
        '''插入'''
        if not root:
            root = TreeNode(val)
        elif val < root.val:
            root.left = self.insert(root.left, val)
        elif val > root.val:
            root.right = self.insert(root.right, val)
        return root

    def query(self, root, val):
        '''查找'''
        if not root:
            return False
        if root.val == val:
            return True
        elif val < root.val:
            return self.query(root.left, val)
        elif val > root.val:
            return self.query(root.right, val)

    def inorder(self, root):
        '''二叉树中序遍历'''
        if not root:
            return []
        else:
            return self.inorder(root.left)+[root.val]+self.inorder(root.right)



    def delNode(self, root, val):
        '''删除二叉搜索树中值为val的点'''
        if not root:
            return
        if val < root.val:
            root.left = self.delNode(root.left, val)
        elif val > root.val:
            root.right = self.delNode(root.right, val)





if __name__ == "__main__" :
    Tree = TreeNode(None)
    li = [17,5,35,2,11,29,38,9,16,8]
    bst_tree = None
    for val in li:
        bst_tree = Tree.insert(bst_tree, val)
    print(Tree.inorder(bst_tree))





