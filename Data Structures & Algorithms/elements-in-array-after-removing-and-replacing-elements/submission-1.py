class Solution:
    def elementInNums(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        HashMap = {} #time:num
        length = 2*len(nums)
        N = nums.copy()
        
        time = 0
        for t in range(len(nums)):
            HashMap[t]=N.copy()
            N.pop(0)
            time+=1
            
        HashMap[time] = []

        tmp = []
        for t in range(len(nums)-1):
            tmp.append(nums[t])
            HashMap[time+t+1] = tmp.copy()

        res = []
        for t,idx in queries:
            TIME = t%length
            if HashMap[TIME] and idx<len(HashMap[TIME]):
                res.append(HashMap[TIME][idx])
            else:
                res.append(-1)

        return res
