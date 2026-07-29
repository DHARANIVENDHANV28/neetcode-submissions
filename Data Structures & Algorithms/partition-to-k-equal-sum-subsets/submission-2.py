class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        SumSubs = sum(nums)//k
        buckets = [0]*k
        if sum(nums)%k != 0:
            return False
        nums.sort(reverse=True)
        def dfs(idx):
            nonlocal buckets
            if idx==len(nums):
                return True

            for j in range(0,k):
                if j>0 and buckets[j] == buckets[j-1]:
                    continue
                if nums[idx]+buckets[j]<=SumSubs:
                    buckets[j] += nums[idx]
                    if dfs(idx+1):
                        return True
                    buckets[j] -= nums[idx] 
            return False
        return dfs(0)
        