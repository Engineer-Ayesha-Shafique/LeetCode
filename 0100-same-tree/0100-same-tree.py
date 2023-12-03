# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        def preorder(node1, node2):
            # Base case: If both nodes are None, they are equal
            if not node1 and not node2:
                return True
            # If one of the nodes is None and the other is not, they are not equal
            if not node1 or not node2:
                return False
            # Check if the values are equal, and recursively check left and right subtrees
            return (node1.val == node2.val) and \
                   preorder(node1.left, node2.left) and \
                   preorder(node1.right, node2.right)

        # Start the preorder traversal from the roots of both trees
        return preorder(p, q)

# Example usage:
# Construct the trees
tree_p = TreeNode(1, TreeNode(2), TreeNode(3))
tree_q = TreeNode(1, TreeNode(2), TreeNode(3))

# Create an instance of the Solution class
solution = Solution()

# Check if the trees are the same
result = solution.isSameTree(tree_p, tree_q)

# Print the result
print(result)
