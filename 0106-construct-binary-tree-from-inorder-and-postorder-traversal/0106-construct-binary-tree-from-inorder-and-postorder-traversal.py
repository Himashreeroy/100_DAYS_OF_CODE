# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder or not postorder:
            return None
        
        # The last element of postorder is the root of the current subtree
        root_val = postorder.pop()
        root = TreeNode(root_val)
        
        # Find the index of the root value in the inorder list
        root_index = inorder.index(root_val)
        
        # Recursively build the right subtree first (since postorder visits root-right-left)
        root.right = self.buildTree(inorder[root_index + 1:], postorder)
        # Recursively build the left subtree
        root.left = self.buildTree(inorder[:root_index], postorder)
        
        return root
