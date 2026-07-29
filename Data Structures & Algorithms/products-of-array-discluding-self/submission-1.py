class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mul = 1
        oz = []
        len_zero = []
        for idx,num in enumerate(nums):
            if num != 0 :
                mul = mul*num
            else:
                oz.append(idx)
                len_zero.append(idx)
                continue
        print("mul",mul)

        Output = []
        if len(oz) == 0 :
            for num in nums:
                ans = mul//num
                Output.append(ans)
            print("1")

        if len(len_zero) == 1 :
            for num in nums:
                if num != 0:
                    ans = 0
                    Output.append(ans)
                if num == 0:
                    ans = mul
                    Output.append(ans)
            print('2')
        
        if len(len_zero) >1:
            Output = [0]*len(nums)
            print("3")
        return Output

            



        