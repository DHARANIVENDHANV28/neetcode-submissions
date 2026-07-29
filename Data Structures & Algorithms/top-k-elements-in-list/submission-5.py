class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        lis = []
        cnt = 0
        for i in nums:
            if i not in hashmap:
                hashmap[i] = cnt+1
            else:
                hashmap[i] += 1
            if hashmap[i] >= k:
                lis.append(i)
        sorted_items = sorted(hashmap.items(), key=lambda x: x[1], reverse=True)

                
        return [key for key,value in sorted_items[:k]]
        