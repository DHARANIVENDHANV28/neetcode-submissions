# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        curr1 = dummy
        curr2 = dummy
        count = 0
        while n+1>count:
            count += 1
            curr2 = curr2.next

        while True:
            if curr2 == None:
                break
            curr1 = curr1.next
            curr2 = curr2.next

        curr1.next = curr1.next.next
        return dummy.next
