class Solution:
    def countElements(self, arr: List[int]) -> int:
        HashMap = {}

        for n in arr:
            if n not in HashMap:
                HashMap[n] = 0
            HashMap[n] += 1

        res = 0

        for i in range(len(arr)):
            if arr[i]+1 in HashMap:
                res += 1
                HashMap[arr[i]+1] -= 1
        
        return res
        