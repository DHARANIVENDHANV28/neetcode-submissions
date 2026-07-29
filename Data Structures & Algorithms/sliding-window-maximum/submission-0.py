class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        Output = []
        for i in range(0,len(nums)-k+1):
            window = nums[i:i+k]
            # print(i,window)
            Output.append(max(window))
        return Output

        