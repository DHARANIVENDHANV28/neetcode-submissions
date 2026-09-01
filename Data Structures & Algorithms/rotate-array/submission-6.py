class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)

        l,r = 0,len(nums)-1
        while l<r:
            nums[l],nums[r] = nums[r],nums[l]
            l+=1
            r-=1
        
        l,r = 0,k-1
        while l<r:
            nums[l],nums[r] = nums[r],nums[l]
            l+=1
            r-=1

        l,r = k,len(nums)-1
        while l<r:
            nums[l],nums[r] = nums[r],nums[l]
            l+=1
            r-=1

        
        

















































        # n = len(nums)
        # tmp = [0]*n

        # for idx,num in enumerate(nums):
        #     tmp[(idx+k)%n] = num
        # nums[:] = tmp
        

            