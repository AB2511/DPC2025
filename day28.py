class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_symmetric(root):
    if not root:
        return True

    def mirror(a, b):
        if not a and not b:
            return True
        if not a or not b:
            return False
        return a.val == b.val and mirror(a.left, b.right) and mirror(a.right, b.left)

    return mirror(root.left, root.right)

t1 = TreeNode(1)
t1.left = TreeNode(2, TreeNode(3), TreeNode(4))
t1.right = TreeNode(2, TreeNode(4), TreeNode(3))
print(is_symmetric(t1))  # True
t2 = TreeNode(1)
t2.left = TreeNode(2, None, TreeNode(3))
t2.right = TreeNode(2, None, TreeNode(3))
print(is_symmetric(t2))  # False

print(is_symmetric(TreeNode(1)))  # True
print(is_symmetric(None))         # True
