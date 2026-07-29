class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        curSum = sum(arr[:k - 1])

        for L in range(len(arr) - k + 1):
            curSum += arr[L + k - 1]
            if (curSum / k) >= threshold:
                res += 1
            curSum -= arr[L]
        return res 
        
        
        
        
        # l = 0
        # res = 0
        # SUM = 0
        # cnt = 0

        # for r in range(len(arr)):

        #     if l > len(arr)-k:
        #         break

        #     SUM += arr[r]
        #     cnt += 1

        #     if cnt == k:
        #         AVG = SUM//k
        #         # print(arr[l:r+1], AVG, threshold)

        #         if AVG >= threshold:
        #             res += 1
        #         cnt -= 1
        #         SUM -= arr[l]
        #         l += 1
        
        # return res
        