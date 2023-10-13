# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # Base case: if the inorder list is empty, return None
        if not inorder:
            return None
        
        # The first element of preorder is the root of the current subtree
        root_val = preorder.pop(0)
        root = TreeNode(root_val)
        
        # Find the index of the root value in the inorder list
        root_index = inorder.index(root_val)
        
        # Recursively build the left and right subtrees based on the root index
        root.left = self.buildTree(preorder, inorder[:root_index])
        root.right = self.buildTree(preorder, inorder[root_index + 1:])
        
        return root
