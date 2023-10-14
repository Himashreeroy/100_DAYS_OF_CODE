# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        def reverseLinkedList(start, end):
            prev, curr = None, start
            while curr != end:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev
        
        def getLength(node):
            length = 0
            while node:
                length += 1
                node = node.next
            return length
        
        length = getLength(head)
        
        if length < k:
            return head
        
        prev, curr = None, head
        for _ in range(k):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        head.next = self.reverseKGroup(curr, k)
        
        return prev
