class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {}  # Dictionary for quick lookup
        self.head = Node(None, None)  # Dummy head node
        self.tail = Node(None, None)  # Dummy tail node
        self.head.next = self.tail  # Connect head to tail
        self.tail.prev = self.head  # Connect tail to head

    def _remove_node(self, node):
        # Remove a node from the doubly linked list
        prev = node.prev
        next_node = node.next
        prev.next = next_node
        next_node.prev = prev

    def _add_node_to_tail(self, node):
        # Add a node to the end of the doubly linked list
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            node = self.cache[key]
            # Move the accessed node to the end of the list (most recently used)
            self._remove_node(node)
            self._add_node_to_tail(node)
            return node.value
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            # Update the value and move the node to the end of the list (most recently used)
            node = self.cache[key]
            node.value = value
            self._remove_node(node)
            self._add_node_to_tail(node)
        else:
            if len(self.cache) >= self.capacity:
                # Remove the least recently used node (head.next)
                del self.cache[self.head.next.key]
                self._remove_node(self.head.next)
            # Add a new node with the given key and value to the end of the list
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_node_to_tail(new_node)
