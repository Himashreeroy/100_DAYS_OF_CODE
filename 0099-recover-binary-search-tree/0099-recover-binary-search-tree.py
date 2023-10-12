# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        # Initialize pointers for Morris Traversal
        curr = root
        prev = None
        first = None
        second = None
        
        # Morris Traversal
        while curr:
            if not curr.left:
                # If there is no left child, visit the current node
                if prev and curr.val < prev.val:
                    # If the current node is out of place, update first and second pointers
                    if not first:
                        first = prev
                    second = curr
                prev = curr
                curr = curr.right  # Move to the right child
            else:
                # Find the inorder predecessor (rightmost node in the left subtree)
                pred = curr.left
                while pred.right and pred.right != curr:
                    pred = pred.right
                
                if not pred.right:
                    # Set the right child of the inorder predecessor to the current node
                    pred.right = curr
                    curr = curr.left  # Move to the left child
                else:
                    # Restore the tree structure and visit the current node
                    pred.right = None
                    if prev and curr.val < prev.val:
                        # If the current node is out of place, update first and second pointers
                        if not first:
                            first = prev
                        second = curr
                    prev = curr
                    curr = curr.right  # Move to the right child
        
        # Swap the values of the out-of-place nodes to recover the BST
        first.val, second.val = second.val, first.val
