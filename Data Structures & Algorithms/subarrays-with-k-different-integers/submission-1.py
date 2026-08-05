class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        HashMap = {}
        res = 0
        ln = 0
        lf = 0

        for r in range(len(nums)):
            if nums[r] not in HashMap:
                HashMap[nums[r]] = 0
            HashMap[nums[r]] += 1

            while len(HashMap) > k:
                HashMap[nums[ln]] -= 1
                if HashMap[nums[ln]] == 0:
                    HashMap.pop(nums[ln])
                ln+=1
                lf=ln
            
            while HashMap[nums[ln]]>1:
                HashMap[nums[ln]] -= 1
                ln+=1
                
            if len(HashMap) == k:
                res += (ln-lf)+1
        return res                