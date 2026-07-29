class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hashmap = {}
        for k in tasks:
            if k not in hashmap:
                hashmap[k] = 1
            else:
                hashmap[k] += 1
        maxheap = [-val for key,val in hashmap.items()]
        heapq.heapify(maxheap)

        time = 0
        q = deque()
        while q or maxheap:
            time+=1
            if not maxheap:
                time = q[0][1]
            else:
                cnt = 1+heapq.heappop(maxheap)
                if cnt:
                    q.append([cnt,time+n])
            if q and q[0][1] == time:
                heapq.heappush(maxheap,q.popleft()[0])
        return time


        