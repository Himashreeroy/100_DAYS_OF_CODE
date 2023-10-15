# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        # Base case: if the node is None, return False
        if not root:
            return False
        
        # Check if it's a leaf node and if its value equals the remaining targetSum
        if not root.left and not root.right and root.val == targetSum:
            return True
        
        # Recur for the left and right subtrees with updated targetSum
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)
