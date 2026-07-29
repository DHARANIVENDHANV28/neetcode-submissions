class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        cur1 = head
        # Use a "while True" and break when we reach the middle
        while True:
            # Find last node and its previous
            prev = None
            cur2 = cur1
            while cur2.next:
                prev = cur2
                cur2 = cur2.next

            # Stop if cur1 is at or next to the last node
            if cur1 == cur2 or cur1.next == cur2:
                break

            # Remove last node
            prev.next = None

            # Insert last node after cur1
            tmp = cur1.next
            cur1.next = cur2
            cur2.next = tmp

            # Move cur1 forward
            cur1 = tmp
