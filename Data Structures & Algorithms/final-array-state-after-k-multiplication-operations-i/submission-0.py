class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        narray = [(val,idx) for idx,val in enumerate(nums)]
        heapq.heapify(narray)

        for _ in range(k):
            minVal,idx = heapq.heappop(narray)
            heapq.heappush(narray,(minVal*multiplier,idx))
            nums[idx] = minVal*multiplier
        return nums
        