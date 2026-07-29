class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # #BubbleSort
        # for i in range(len(nums)-1):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]>nums[j]:
        #             nums[i],nums[j] = nums[j],nums[i]
        # return nums

        #BcuketSort
        bucket = [0]*3
        for n in nums:
            bucket[n] += 1
        
        index = 0
        for i in range(0,3):
            while bucket[i]:
                bucket[i] -= 1
                nums[index] = i
                index += 1
        