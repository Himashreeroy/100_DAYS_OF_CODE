from collections import deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        result = []
        queue = deque([root])
        
        while queue:
            level_nodes = []
            level_size = len(queue)
            
            for _ in range(level_size):
                node = queue.popleft()
                level_nodes.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(level_nodes)
        
        # Reverse the resulting list to get bottom-up level order traversal
        return result[::-1]
