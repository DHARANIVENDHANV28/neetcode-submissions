class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        i = 0
        j = 0
        Output = []
        while i < len(temperatures)-1:
            print(i,j)
            if temperatures[j]>temperatures[i]:
                Output.append(j-i)
                i = i + 1
                j = i + 1
                continue
            if j == len(temperatures)-1:
                Output.append(0)
                i = i + 1
                j = i + 1
            else:
                j += 1
        Output.append(0)
        return Output