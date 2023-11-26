class Solution:
    #Function to remove a loop in the linked list.
    def removeLoop(self, head):
        
        #using two pointers and moving one pointer(slow) by one node and 
        #another pointer(fast) by two nodes in each iteration.
        fast = head.next
        slow = head
        
        while fast!=slow:
            
            #if the node pointed by first pointer(fast) or the node 
            #next to it is null, then loop is not present so we return 0.
            if fast is None or fast.next is None:
                return
            
            fast = fast.next.next
            slow = slow.next
            
        #both pointers now point to the same node in the loop.
        
        size = 1
        fast = fast.next
    
        #we start iterating the loop with first pointer and continue till 
        #both pointers point to same node again.
        while fast!=slow:
            fast = fast.next
            #incrementing the counter which stores length of loop.
            size+=1
        
        #updating the pointers again to starting node.
        slow=head
        fast=head
        
        #moving pointer (fast) by (size-1) nodes.
        for _ in range(size-1):
            fast=fast.next
        
        #now we keep iterating with both pointers till fast reaches a node such
        #that the next node is pointed by slow. At this situation slow is at
        #the node where loop starts and first at last node so we simply 
        #update the link part of first.
        while fast.next != slow:
            fast=fast.next
            slow=slow.next
        
        #storing null in link part of the last node.
        fast.next=None

#{ 
 # Driver Code Starts
# driver code:

class Node:
    def __init__(self,val):
        self.next=None
        self.data=val

class linkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def add(self,num):
        if self.head is None:
            self.head=Node(num)
            self.tail=self.head
        else:
            self.tail.next=Node(num)
            self.tail=self.tail.next
    
    def isLoop(self):
        if self.head is None:
            return False
        
        fast=self.head.next
        slow=self.head
        
        while slow != fast:
            if fast is None or fast.next is None:
                return False
            fast=fast.next.next
            slow=slow.next
        
        return True
    
    def loopHere(self,position):
        if position==0:
            return
        
        walk=self.head
        for _ in range(1,position):
            walk=walk.next
        self.tail.next=walk
    
    def length(self):
        walk=self.head
        ret=0
        while walk:
            ret+=1
            walk=walk.next
        return ret

if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=tuple(int(x) for x in input().split())
        pos=int(input())
        
        ll = linkedList()
        for i in arr:
            ll.add(i)
        ll.loopHere(pos)
        
        Solution().removeLoop(ll.head)
        
        if ll.isLoop() or ll.length()!=n:
            print(0)
            continue
        else:
            print(1)

# } Driver Code Ends