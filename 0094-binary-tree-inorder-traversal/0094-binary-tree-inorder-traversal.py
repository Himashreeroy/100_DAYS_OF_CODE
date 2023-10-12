class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        stack = []
        current = root
        
        while current or stack:
            # Traverse to the leftmost node and push nodes along the way onto the stack
            while current:
                stack.append(current)
                current = current.left
            
            # Pop a node from the stack, add its value to the result, and move to its right child
            current = stack.pop()
            result.append(current.val)
            current = current.right
        
        return result

        