class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        INC,DEC = True,True

        for i in range(len(nums)-1):
            if not (nums[i] <= nums[i+1]):
                INC = False
            if not (nums[i] >= nums[i+1]):
                DEC = False
            print(nums[i],nums[i+1],INC,DEC)

        return INC or DEC
        


            

        