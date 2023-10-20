# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node, current_sum):
            if not node:
                return 0
            
            # Calculate the current number represented by the path from the root to this node
            current_sum = current_sum * 10 + node.val
            
            # If it's a leaf node, add the number to the total sum
            if not node.left and not node.right:
                return current_sum
            
            # Otherwise, continue DFS to the left and right children
            left_sum = dfs(node.left, current_sum)
            right_sum = dfs(node.right, current_sum)
            
            # Return the sum of numbers represented by paths in the left and right subtrees
            return left_sum + right_sum
        
        return dfs(root, 0)
