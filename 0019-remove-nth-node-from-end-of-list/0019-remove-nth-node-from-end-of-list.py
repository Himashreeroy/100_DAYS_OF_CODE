class Solution:
    def removeNthFromEnd(self, head, n):
        # Create a dummy node to handle the case when the head needs to be removed
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy

        # Move the first pointer n+1 steps ahead
        for i in range(n + 1):
            first = first.next

        # Move both pointers simultaneously until the first pointer reaches the end
        while first is not None:
            first = first.next
            second = second.next

        # Remove the nth node by updating the next pointer of the (n-1)th node
        second.next = second.next.next

        return dummy.next
