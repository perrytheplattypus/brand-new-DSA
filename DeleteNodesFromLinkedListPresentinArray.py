from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        # Convert nums array into a set for efficient lookup
        num_set = set(nums)
        
        # Initialize a dummy node to handle edge cases (like removing the head node)
        dummy = ListNode(0)
        dummy.next = head
        
        # prev and curr pointers for traversal
        prev, curr = dummy, head
        
        # Traverse the list
        while curr:
            # If current node's value is in num_set, skip it
            if curr.val in num_set:
                prev.next = curr.next
            else:
                # Otherwise, move the prev pointer forward
                prev = curr
            # Move to the next node
            curr = curr.next
        
        # Return the modified list, starting from the node after dummy
        return dummy.next
