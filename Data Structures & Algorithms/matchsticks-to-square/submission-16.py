class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if sum(matchsticks)%4 != 0:
            return False
        side = sum(matchsticks)//4
        matchsticks.sort(reverse=True)
        sub = [0]*4
        def dfs(idx):
            #BC
            if idx == len(matchsticks):
                return sub[0]==sub[1]==sub[2]==sub[3]==side 
            for i in range(4):
                if matchsticks[idx]+sub[i] > side:
                    continue
                sub[i]+=matchsticks[idx]
                if dfs(idx+1):
                    return True
                sub[i]-=matchsticks[idx]
            return False
        
        return dfs(0)




















































        # length = sum(matchsticks)/4
        # if sum(matchsticks) %4 != 0:
        #     return False
        # sides = [0]*4
        # matchsticks.sort(reverse=True)
        # def dfs(idx):
        #     if idx == len(matchsticks):
        #         return sides[0] == sides[1] == sides[2] == sides[3]
            
        #     for j in range(4):
        #         if sides[j] + matchsticks[idx] <= length:
        #             sides[j] += matchsticks[idx]
        #             if dfs(idx+1):
        #                 return True
        #             sides[j] -= matchsticks[idx]


        #     return False
        # return dfs(0)
        