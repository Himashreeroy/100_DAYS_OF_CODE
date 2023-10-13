# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def getHeight(node):
            if not node:
                return 0
            left_height = getHeight(node.left)
            right_height = getHeight(node.right)
            
            # If any subtree is not balanced, return -1 to indicate it's not balanced
            if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
                return -1
            
            # Return the height of the current subtree
            return 1 + max(left_height, right_height)
        
        return getHeight(root) != -1

        