# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to simplify edge cases
        dummy = ListNode(0)
        dummy.next = head
        prev, current = dummy, head

        while current:
            # Check for duplicate nodes
            if current.next and current.val == current.next.val:
                # Skip all nodes with duplicate values
                while current.next and current.val == current.next.val:
                    current = current.next
                # Move to the next distinct node
                current = current.next
                prev.next = current
            else:
                # Move to the next node
                prev = prev.next
                current = current.next

        return dummy.next
