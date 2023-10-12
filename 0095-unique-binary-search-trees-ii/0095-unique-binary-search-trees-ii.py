class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def generate_trees_helper(start, end):
            trees = []
            if start > end:
                trees.append(None)
                return trees
            
            for i in range(start, end + 1):
                left_trees = generate_trees_helper(start, i - 1)
                right_trees = generate_trees_helper(i + 1, end)
                
                for left in left_trees:
                    for right in right_trees:
                        root = TreeNode(i)
                        root.left = left
                        root.right = right
                        trees.append(root)
                        
            return trees
        
        if n == 0:
            return []
        
        return generate_trees_helper(1, n)
