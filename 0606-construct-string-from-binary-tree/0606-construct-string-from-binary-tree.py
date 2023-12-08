# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def tree2str(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        def preorder(node):
            if not node:
                return ""

            result = str(node.val)

            left_str = preorder(node.left)
            right_str = preorder(node.right)

            if not left_str and not right_str:
                return result
            elif not right_str:
                return result + "(" + left_str + ")"
            else:
                return result + "(" + left_str + ")" + "(" + right_str + ")"

        return preorder(root)

