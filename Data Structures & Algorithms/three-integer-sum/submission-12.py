class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        S_nums = sorted(nums)
        Output = []
        for idx_i in range(0,len(S_nums)-2):
            target = -1*S_nums[idx_i]
            for idx_j in range(idx_i+1,len(S_nums)-1):
                print(idx_i,idx_j)
                k = target-S_nums[idx_j]
                if k not in S_nums[idx_j+1:]:
                    continue
                else:
                    Output.append([S_nums[idx_i],S_nums[idx_j],k]) 
        Output_ = []
        for out in Output:
            if out not in Output_:
                Output_.append(out)
        return Output_
        

            