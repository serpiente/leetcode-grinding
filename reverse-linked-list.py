# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        previous = None
        current = head
        following = head.next

        while current:
            current.next = previous
            previous = current
            current = following
            if following:
                following = following.next
        return previous

