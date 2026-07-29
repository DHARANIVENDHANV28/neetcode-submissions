class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        HashMap = {}

        for n in nums:
            if n not in HashMap:
                HashMap[n] = 1
            else:
                HashMap[n] += 1
        
        for key,val in HashMap.items():
            if val %2 != 0:
                return False
        return True

        