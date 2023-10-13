# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Base case: if the node is None, the depth is 0
        if not root:
            return 0
        
        # Recursive step: calculate the maximum depth of the left and right subtrees
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        
        # Return the maximum depth of the current node by adding 1 (for the current node itself)
        # to the maximum depth of its subtrees
        return max(left_depth, right_depth) + 1
