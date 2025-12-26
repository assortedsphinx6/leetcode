# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # reverse list
        tail = None

        while head:
            head.next, tail, head = tail, head, head.next

        prev = tail
        prev.next, tail = None, tail.next

        # only keep larger values
        while tail:
            if tail.val >= prev.val:
                tail.next, prev, tail = prev, tail, tail.next
            else:
                tail = tail.next

        return prev
