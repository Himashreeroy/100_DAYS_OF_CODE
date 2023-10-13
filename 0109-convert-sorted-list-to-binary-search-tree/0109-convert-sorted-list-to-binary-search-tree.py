# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[TreeNode]
        """
        # Convert the linked list to an array
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        
        # Helper function to build BST from sorted array
        def sortedArrayToBST(left, right):
            if left > right:
                return None
            
            mid = (left + right) // 2
            root = TreeNode(nums[mid])
            root.left = sortedArrayToBST(left, mid - 1)
            root.right = sortedArrayToBST(mid + 1, right)
            return root
        
        return sortedArrayToBST(0, len(nums) - 1)
