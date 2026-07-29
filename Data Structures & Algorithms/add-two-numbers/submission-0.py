# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        cur1 = l1
        cur2 = l2
        cf = 0
        while cur1 or cur2 or cf:
            val1 = cur1.val if cur1 else 0
            val2 = cur2.val if cur2 else 0
            Sum = val1+val2+cf
            cf = Sum//10
            digit = Sum%10
            cur.next = ListNode(digit)
            cur = cur.next

            cur1 = cur1.next if cur1 else None
            cur2 = cur2.next if cur2 else None
        return dummy.next
      
        