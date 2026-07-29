class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums)-1
        output = [0]*len(nums)

        for n in nums:
            if l<=r:
                if n % 2 == 0:
                    output[l] = n
                    l += 1
                else:
                    output[r] = n
                    r -= 1
            else:
                break

        return output