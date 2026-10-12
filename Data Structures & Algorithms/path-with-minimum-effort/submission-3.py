class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:

        ROWS,COLS = len(heights),len(heights[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        minHeap = [(0,0,0)] #(cost,row,col)
        visited = set()
        res = 0
        while minHeap:
            diff,r,c = heapq.heappop(minHeap)
            if (r,c) in visited:
                continue
            res = max(res,diff)
            visited.add((r,c))
            if (r,c) == (ROWS-1,COLS-1):
                return res
            for dr,dc in directions:
                nr,nc = r+dr,c+dc
                if nr<0 or nc<0 or nr>=ROWS or nc>=COLS or (nr,nc) in visited:
                    continue
                newdiff = abs(heights[r][c]-heights[nr][nc])
                heapq.heappush(minHeap,(newdiff,nr,nc))
                
        