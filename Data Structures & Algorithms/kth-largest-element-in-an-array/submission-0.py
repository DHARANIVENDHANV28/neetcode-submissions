class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        MinHeap = nums
        heapq.heapify(MinHeap)
        while len(MinHeap)>k:
            heapq.heappop(MinHeap)
        return MinHeap[0]

        