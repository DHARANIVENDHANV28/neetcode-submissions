class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        minProtime = [[t[1],t[0],idx] for idx,t in enumerate(tasks)]
        heapq.heapify(minProtime)
        s_tasks = sorted(tasks)
        time = s_tasks[0][0]
        res = []

        for _ in range(len(tasks)):
            tmp = []
            p,e,i = heapq.heappop(minProtime)
            print([e,p],"*")
            if time < e:
                tmp = [[p,e,i]]
            while minProtime and time < e:  
                p,e,i = heapq.heappop(minProtime)
                print([e,p])
                if time < e:
                    tmp.append([p,e,i])
            # p1,e1,i1 = heapq.heappop(minProtime)
            res.append(i)
            time += p
            if tmp:
                for e in tmp:
                    heapq.heappush(minProtime,e)
        return res

