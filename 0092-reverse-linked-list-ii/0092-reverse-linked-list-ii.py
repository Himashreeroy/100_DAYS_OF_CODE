class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        # Create a dummy node to handle edge cases
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        
        # Move to the node before the left position
        for _ in range(left - 1):
            prev = prev.next
        
        # Initialize pointers for reversing the sublist
        current = prev.next
        next_node = None
        
        # Reverse the sublist from left to right
        for _ in range(right - left + 1):
            next_temp = current.next
            current.next = next_node
            next_node = current
            current = next_temp
        
        # Connect the reversed sublist with the original list
        prev.next.next = current
        prev.next = next_node
        
        return dummy.next
