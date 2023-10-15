# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # If the tree is empty, the depth is 0
        if not root:
            return 0
        
        # If the current node is a leaf, return 1
        if not root.left and not root.right:
            return 1
        
        # Calculate the minimum depth of the left and right subtrees
        left_depth = float('inf') if not root.left else self.minDepth(root.left)
        right_depth = float('inf') if not root.right else self.minDepth(root.right)
        
        # Return the minimum depth of the current node by adding 1 to the minimum of left and right subtrees
        return min(left_depth, right_depth) + 1
