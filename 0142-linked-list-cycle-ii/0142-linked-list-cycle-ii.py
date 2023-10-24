# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Step 1: Detect if there is a cycle using slow and fast pointers
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                break
        else:
            # No cycle detected
            return None
        
        # Step 2: Reset one pointer to the head and move both pointers one step at a time
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        
        # Now slow and fast pointers meet at the start of the cycle
        return slow
