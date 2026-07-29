class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l = 0
        res = 0
        SUM = 0
        cnt = 0

        for r in range(len(arr)):

            if l > len(arr)-k:
                break

            SUM += arr[r]
            cnt += 1

            if cnt == k:
                AVG = SUM//k
                # print(arr[l:r+1], AVG, threshold)

                if AVG >= threshold:
                    res += 1
                cnt -= 1
                SUM -= arr[l]
                l += 1
        
        return res
        