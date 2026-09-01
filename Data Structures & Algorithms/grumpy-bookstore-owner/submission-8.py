class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:

        satisfied = 0
        max_window,window = 0,0
        l = 0
        for r in range(len(customers)):
            if grumpy[r]:
                window += customers[r]
            else:
                satisfied += customers[r]
            
            if r-l+1 > minutes:
                if grumpy[l]:
                    window -= customers[l]
                l+=1
            
            max_window = max(max_window,window)
        
        return satisfied + max_window
        