class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        tmp = [0]*n

        for idx,num in enumerate(nums):
            tmp[(idx+k)%n] = num
        nums[:] = tmp
        

            