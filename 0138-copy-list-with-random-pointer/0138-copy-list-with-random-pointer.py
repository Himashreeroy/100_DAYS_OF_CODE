class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        # Create a dictionary to store the mapping from original nodes to new nodes
        mapping = {}
        
        # First pass: create new nodes and store them in the dictionary
        current = head
        while current:
            mapping[current] = Node(current.val)
            current = current.next
        
        # Second pass: update next and random pointers in the new nodes
        current = head
        while current:
            if current.next:
                mapping[current].next = mapping[current.next]
            if current.random:
                mapping[current].random = mapping[current.random]
            current = current.next
        
        # Return the head of the new linked list
        return mapping.get(head, None)
