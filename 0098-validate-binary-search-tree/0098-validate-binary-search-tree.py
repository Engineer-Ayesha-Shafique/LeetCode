# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root, minVal=float('-inf'), maxVal=float('inf')):
        if not root:
            return True
        if root.val <= minVal or root.val >= maxVal:
            return False
        return Solution().isValidBST(root.left, minVal, root.val) and Solution().isValidBST(root.right, root.val, maxVal)