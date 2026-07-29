class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        HashMap = {}
        for i,t in enumerate(tickets):
            HashMap[i] = t
        
        time = 0
        cnt = 0
        while HashMap[k] != 0:
            idx = cnt%len(HashMap)
            # print(HashMap)
            if HashMap[idx] != 0:
                HashMap[idx]-=1
                time+=1
            cnt+=1
        return time

        