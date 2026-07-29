class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)
        while len(self.nums)>self.k:
            heapq.heappop(self.nums)

        
        
    def add(self, val: int) -> int:
        heapq.heappush(self.nums,val)
        while len(self.nums)>self.k:
            heapq.heappop(self.nums)
        return self.nums[0]

    # def __init__(self, k: int, nums: List[int]):
    #     self.k = k
    #     self.nums = nums
        
        
    # def add(self, val: int) -> int:
    #     #adding number
    #     self.nums.append(val)
        
    #     #heapify
    #     self.num = [-n for n in self.nums]
    #     heapq.heapify(self.num)
        
    #     #returning kth largest number
    #     i = 0
    #     while self.k>i+1:   
    #         heapq.heappop(self.num)
    #         i+=1
    
    #     return -heapq.heappop(self.num)

        
