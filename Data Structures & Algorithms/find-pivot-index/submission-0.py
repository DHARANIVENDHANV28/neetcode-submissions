class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        Nums = [0]+nums+[0]
        SUM = sum(Nums)
        PSUM = 0

        for idx in range(1,len(Nums)-1):
            PSUM += Nums[idx-1]
            RSUM = SUM - PSUM - Nums[idx]
            print(PSUM,RSUM)
            if PSUM == RSUM:
                return idx-1
        return -1
        