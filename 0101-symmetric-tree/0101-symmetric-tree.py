class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def isMirror(left, right):
            # Base case: If both nodes are None, they are symmetric.
            if not left and not right:
                return True
            # If one of the nodes is None or the values are different, they are not symmetric.
            if not left or not right or left.val != right.val:
                return False
            # Recursively check the subtrees in a mirror fashion.
            return isMirror(left.left, right.right) and isMirror(left.right, right.left)

        # Check if the tree is symmetric starting from the root.
        return not root or isMirror(root.left, root.right)
