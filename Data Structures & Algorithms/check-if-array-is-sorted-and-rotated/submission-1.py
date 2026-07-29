class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        arr = [0]*n
        sorted_nums = sorted(nums)
        
        for x in range(0,n):
            for i in range(0,n):
                arr[i] = sorted_nums[(i+x)%n]
            if arr == nums:
                return True
        return False

        