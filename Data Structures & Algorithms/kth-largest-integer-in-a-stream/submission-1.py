class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        
        
    def add(self, val: int) -> int:
        self.nums.append(val)
        self.num = [-n for n in self.nums]
        heapq.heapify(self.num)
        #adding number
        # heapq.heappush(self.num,-val)

        #returning kth largest number
        i = 0
        while self.k>i+1:   
            heapq.heappop(self.num)
            i+=1
    
        return -heapq.heappop(self.num)

        
