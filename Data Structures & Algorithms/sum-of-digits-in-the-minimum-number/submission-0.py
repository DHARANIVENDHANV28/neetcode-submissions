class Solution:
    def sumOfDigits(self, nums: List[int]) -> int:
        #even -> 1, odd -> 0
        smallest_val = min(nums)
        sum_val = 0
        for d in str(smallest_val):
            sum_val += int(d)
        
        return 1 if sum_val%2==0 else 0
