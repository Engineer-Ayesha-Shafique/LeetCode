# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        if not root:
            return False

        # Helper function to check if two trees are identical
        def is_identical(tree1, tree2):
            if not tree1 and not tree2:
                return True
            if not tree1 or not tree2:
                return False
            return (
                tree1.val == tree2.val
                and is_identical(tree1.left, tree2.left)
                and is_identical(tree1.right, tree2.right)
            )

        # Check if the current subtree starting from root is identical to subRoot
        if is_identical(root, subRoot):
            return True

        # Recursively check if subRoot is a subtree of the left or right subtree
        return (
            self.isSubtree(root.left, subRoot) or
            self.isSubtree(root.right, subRoot)
        )
