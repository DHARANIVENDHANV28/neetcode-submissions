class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if not digits:
            return [1]

        if digits[-1] < 9:
            digits[-1]+=1
            return digits
        else:
            return self.plusOne(digits[:-1])+[0]

        # def dfs(i,c):
        #     if i < 0 and c ==1:
        #         digits[0] = 0
        #         digits.insert(0,c)
        #         return digits
        #     inc = digits[i]+c
        #     if inc < 10:
        #         digits[i] = inc 
        #         return digits
        #     if inc == 10:
        #         digits[i] = 0
        #         carry = 1
        #         return dfs(i-1,carry)
        # i = len(digits)-1
        
        # if digits[i]+1 < 10:
        #     digits[i] = digits[i]+1
        #     return digits
        # if digits[i]+1 == 10:
        #     return dfs(i,1)


        