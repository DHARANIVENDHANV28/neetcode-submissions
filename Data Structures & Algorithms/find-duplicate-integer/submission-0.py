class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        cur1 = 0
        while cur1 < len(nums)-1:
            cur2 = cur1+1
            while cur2<len(nums):
                if nums[cur1] == nums[cur2]:
                    return nums[cur1]
                else:
                    cur2 += 1
            cur1+=1
        return 0
        
        