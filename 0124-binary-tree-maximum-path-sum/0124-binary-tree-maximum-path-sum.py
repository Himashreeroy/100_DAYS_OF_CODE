# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def maxPathSumHelper(node):
            if not node:
                return 0
            
            # Calculate the maximum path sum that ends at the current node
            left_sum = max(maxPathSumHelper(node.left), 0)
            right_sum = max(maxPathSumHelper(node.right), 0)
            
            # Update the global maximum path sum considering paths that can include the current node
            self.max_sum = max(self.max_sum, node.val + left_sum + right_sum)
            
            # Return the maximum path sum that can be extended from the current node
            return node.val + max(left_sum, right_sum)
        
        # Initialize the global maximum path sum
        self.max_sum = float('-inf')
        maxPathSumHelper(root)
        
        return self.max_sum
