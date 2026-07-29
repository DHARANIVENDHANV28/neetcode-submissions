class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        arr = sorted(nums)
        right = len(nums)-1
        left = 0
        while left < right:
            if arr[left] != arr[left+1] and arr[right] != arr[right-1]:
                right -= 1
                left += 1
            else:
                return True
        print(left,right)
        if  left >= right:
            return False

         