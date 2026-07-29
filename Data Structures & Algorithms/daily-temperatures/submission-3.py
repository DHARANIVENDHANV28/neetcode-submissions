class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        Output = []
        for i in range(0,len(temperatures)-1):
            for j in range(i+1,len(temperatures)):
                diff = temperatures[j]-temperatures[i]
                if diff > 0:
                    Output.append(j-i)
                    break
                elif j>=len(temperatures)-1:
                    Output.append(0)
                else:
                    continue

        Output.append(0)
        return Output


        