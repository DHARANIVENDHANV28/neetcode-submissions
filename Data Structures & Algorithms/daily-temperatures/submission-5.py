class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0]*len(temperatures)
        stack = [] #(idx,temp)
        for i,t in enumerate(temperatures):
            while stack and stack[-1][1] < t:
                idx,temp = stack.pop()
                output[idx] = i-idx
            stack.append((i,t))
        return output
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
        # Output = [0]*len(temperatures)
        # stack = [] #(idx,temp)
        # for idx,temp in enumerate(temperatures):
        #     while stack and stack[-1][1] < temp:
        #         i,t = stack.pop()
        #         Output[i] = idx-i
        #     stack.append((idx,temp))
        # return Output

        


        