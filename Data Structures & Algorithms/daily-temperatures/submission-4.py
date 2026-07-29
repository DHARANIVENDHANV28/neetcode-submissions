class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        Output = [0]*len(temperatures)
        stack = [] #(idx,temp)
        for idx,temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                i,t = stack.pop()
                Output[i] = idx-i
            stack.append((idx,temp))
        return Output

        


        