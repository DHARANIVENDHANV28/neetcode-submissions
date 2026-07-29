class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        INC,DEC = False,False
        STACK = [nums[0]]
        for i in range(1,len(nums)):
            if STACK[-1] <= nums[i]:
                STACK.append(nums[i])
        INC = True if len(STACK) == len(nums) else False
        STACK = [nums[0]]
        for i in range(1,len(nums)):
            if STACK[-1] >= nums[i]:
                STACK.append(nums[i])
        DEC = True if len(STACK) == len(nums) else False

        return True if INC or DEC else False


            

        