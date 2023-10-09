class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Step 1: Find the length of the linked list
        if not head or not head.next:
            return head
        
        length = 1
        current = head
        while current.next:
            current = current.next
            length += 1
        
        # Step 2: Update k to k % length
        k %= length
        
        # Step 3: Connect the last node to the first node to create a circular linked list
        current.next = head
        
        # Step 4: Traverse to the node at (length - k)th position
        for _ in range(length - k):
            current = current.next
        
        # Step 5: Update the head of the linked list and break the circular linkage
        new_head = current.next
        current.next = None
        
        return new_head
 