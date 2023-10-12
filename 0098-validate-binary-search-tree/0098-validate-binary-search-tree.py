# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def inorder_traversal(node, prev):
            if not node:
                return True
            
            # Traverse the left subtree
            if not inorder_traversal(node.left, prev):
                return False
            
            # Check if the current node's value is greater than the previous node's value
            if node.val <= prev[0]:
                return False
            
            prev[0] = node.val  # Update the previous node's value
            
            # Traverse the right subtree
            return inorder_traversal(node.right, prev)
        
        prev = [-float('inf')]  # Initialize prev with negative infinity
        return inorder_traversal(root, prev)

        