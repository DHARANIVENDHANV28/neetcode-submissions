class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_mul = []
        pre_mul = 1
        for ele in nums:
            pre_mul = pre_mul*ele
            prefix_mul.append(pre_mul)
        print(prefix_mul)
            
        postfix_mul = []
        post_mul = 1
        for ele in nums[::-1]:
            post_mul = post_mul*ele
            postfix_mul.append(post_mul)
        postfix_mul = postfix_mul[::-1]
        print(postfix_mul)
        Output = []
        for idx,ele in enumerate(nums):
            if (idx-1) < 0:
                Output.append(postfix_mul[1])
            if idx >0 and idx < len(nums)-1:
                Output.append(prefix_mul[idx-1]*postfix_mul[idx+1])
            if (idx+1) == len(nums):
                Output.append(prefix_mul[len(nums)-2])
        return Output


            

            



        