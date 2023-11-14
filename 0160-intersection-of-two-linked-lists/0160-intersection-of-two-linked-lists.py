# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None

        # Helper function to get the length of a linked list
        def getLength(node):
            length = 0
            while node:
                length += 1
                node = node.next
            return length

        # Get the lengths of both linked lists
        lengthA = getLength(headA)
        lengthB = getLength(headB)

        # Move the pointer of the longer linked list to make them start at the same position
        while lengthA > lengthB:
            headA = headA.next
            lengthA -= 1

        while lengthB > lengthA:
            headB = headB.next
            lengthB -= 1

        # Traverse both linked lists until they intersect
        while headA != headB:
            headA = headA.next
            headB = headB.next

        # Return the intersection node (or None if there is no intersection)
        return headA
