class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        
        if total % k != 0:
            return False
        
        target = total // k
        buckets = [0] * k
        
        nums.sort(reverse=True)
        
        def dfs(idx):
            if idx == len(nums):
                return True
            
            for j in range(k):
                # skip duplicate bucket states
                if j > 0 and buckets[j] == buckets[j - 1]:
                    continue
                
                if buckets[j] + nums[idx] <= target:
                    buckets[j] += nums[idx]
                    
                    if dfs(idx + 1):
                        return True
                    
                    buckets[j] -= nums[idx]
            
            return False
        
        return dfs(0)