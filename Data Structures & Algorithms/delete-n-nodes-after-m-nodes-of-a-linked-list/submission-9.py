# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteNodes(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        cur = head
       
        while cur:
            for _ in range(1,m):
                if cur is None:
                    return head
                cur = cur.next
            if cur is None:
                break
            nxt = cur.next
            for _ in range(n):
                if nxt is None:
                    break
                nxt = nxt.next

            cur.next = nxt
            cur = nxt
        return head 