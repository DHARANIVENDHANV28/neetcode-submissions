class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        sol,res = [],[]

        def BT():
            if len(sol) == len(nums):
                res.append(sol.copy())
                return 
            
            for i in nums:
                if i not in sol:
                    sol.append(i)
                    BT()
                    sol.pop()
        
        BT()
        return res
        