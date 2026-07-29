class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        HashMap = {}

        for i in nums:
            HashMap[i] = 0
        for i in range(len(nums)):
            if nums[i] in HashMap:
                HashMap[nums[i]] = max(HashMap[nums[i]],len(nums)-i)
        print(HashMap)
        val = len(nums)
        for i in range(0,max(nums)+1):
            if i not in HashMap:
                HashMap[i] = val
            else:
                val = HashMap[i]-1
            if HashMap[i]==i:
                return i
        return -1

