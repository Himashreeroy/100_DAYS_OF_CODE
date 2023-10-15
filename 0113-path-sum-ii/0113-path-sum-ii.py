# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        def dfs(node, targetSum, path, result):
            if not node:
                return
            
            # Add the current node's value to the path
            path.append(node.val)
            
            # If it's a leaf node and its value equals the remaining targetSum, add the path to the result
            if not node.left and not node.right and node.val == targetSum:
                result.append(list(path))  # Add a copy of the path to the result
            
            # Recur for the left and right subtrees with updated targetSum and path
            dfs(node.left, targetSum - node.val, path, result)
            dfs(node.right, targetSum - node.val, path, result)
            
            # Backtrack: remove the current node's value from the path
            path.pop()
        
        result = []  # List to store the result paths
        dfs(root, targetSum, [], result)  # Start DFS from the root
        
        return result
