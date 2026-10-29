# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur  = head
        while cur and cur.next:
            nxt = cur.next
            if cur.val == nxt.val:
                cur.next = nxt.next
            else:
                cur.next = nxt
                cur = nxt
        return head
        