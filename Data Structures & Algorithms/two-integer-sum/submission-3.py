class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        HashMap = {}

        for idx,val in enumerate(nums):
            diff = target - val

            if diff in HashMap:
                return [HashMap[diff],idx]
            else:
                HashMap[val] = idx