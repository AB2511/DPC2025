class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_bst(node, min_val=float("-inf"), max_val=float("inf")):
    if node is None:
        return True

    if node.val <= min_val or node.val >= max_val:
        return False

    if not is_bst(node.left, min_val, node.val):
        return False
    if not is_bst(node.right, node.val, max_val):
        return False

    return True

root1 = TreeNode(2, TreeNode(1), TreeNode(3))
print(is_bst(root1))  # True

root2 = TreeNode(5)
root2.left = TreeNode(1)
root2.right = TreeNode(4, TreeNode(3), TreeNode(6))
print(is_bst(root2))  # False

root3 = TreeNode(10)
root3.left = TreeNode(5)
root3.right = TreeNode(15, TreeNode(6), TreeNode(20))
print(is_bst(root3))  # False

print(is_bst(TreeNode(42)))  # True

dup = TreeNode(2, TreeNode(2), None)
print(is_bst(dup))  # False
