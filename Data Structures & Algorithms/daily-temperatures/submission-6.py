class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] #[temp,idx]
        output = [0]*len(temperatures)

        for cur_idx,temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                t,idx = stack.pop()
                output[idx] = cur_idx-idx
            stack.append([temp,cur_idx])
        return output     

       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
        # Output = [0]*len(temperatures)
        # stack = [] #(idx,temp)
        # for idx,temp in enumerate(temperatures):
        #     while stack and stack[-1][1] < temp:
        #         i,t = stack.pop()
        #         Output[i] = idx-i
        #     stack.append((idx,temp))
        # return Output

        


        