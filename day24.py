class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lca(root, p, q):
    if root is None:
        return None
    if root == p or root == q:
        return root

    left = lca(root.left, p, q)
    right = lca(root.right, p, q)

    if left and right:
        return root
    return left or right

def sample_tree():
    #      3
    #    /   \
    #   5     1
    #  / \   / \
    # 6   2 0   8
    #    / \
    #   7   4
    n3 = TreeNode(3)
    n5, n1 = TreeNode(5), TreeNode(1)
    n6, n2 = TreeNode(6), TreeNode(2)
    n0, n8 = TreeNode(0), TreeNode(8)
    n7, n4 = TreeNode(7), TreeNode(4)

    n3.left, n3.right = n5, n1
    n5.left, n5.right = n6, n2
    n1.left, n1.right = n0, n8
    n2.left, n2.right = n7, n4
    return n3, n5, n1, n6, n2, n0, n8, n7, n4

root, n5, n1, n6, n2, n0, n8, n7, n4 = sample_tree()
print(lca(root, n5, n1).val)  # 3
print(lca(root, n5, n4).val)  # 5
print(lca(root, n1, n0).val)  # 1
print(lca(root, n6, n4).val)  # 5
print(lca(root, n7, n8).val)  # 3
# tiny tree
r = TreeNode(1)
r.left = TreeNode(2)
print(lca(r, r, r.left).val)  # 1
