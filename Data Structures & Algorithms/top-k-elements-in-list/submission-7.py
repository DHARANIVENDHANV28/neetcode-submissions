class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        Bucket = [[] for _ in range(len(nums)+1)]
        result = []
        for n in nums:
            if n not in hashmap:
                hashmap[n] = 1
            else:
                hashmap[n] += 1

        for num,count in hashmap.items():
            Bucket[count].append(num)

        for c in range(len(Bucket)-1,-1,-1):
            for n in Bucket[c]:
                result.append(n)
            if len(result) == k:
                return result 
        
                
                
            