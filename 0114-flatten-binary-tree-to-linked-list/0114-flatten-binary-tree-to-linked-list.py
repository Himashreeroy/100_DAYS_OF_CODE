# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        
        # Store the right subtree
        right_subtree = root.right
        
        # Flatten the left subtree
        self.flatten(root.left)
        
        # After flattening the left subtree, the root's right should point to the flattened left subtree
        root.right = root.left
        
        # Set the left subtree to None
        root.left = None
        
        # Move to the end of the current flattened subtree to attach the right subtree
        while root.right:
            root = root.right
        
        # Attach the original right subtree
        root.right = right_subtree
        
        # Flatten the original right subtree
        self.flatten(right_subtree)
