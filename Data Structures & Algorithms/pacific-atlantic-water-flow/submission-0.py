class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        rows, cols = len(heights), len(heights[0])
        
        pacific = set()
        atlantic = set()
        
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        def dfs(r, c, visited):
            visited.add((r,c))
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if (0 <= nr < rows and 
                    0 <= nc < cols and
                    (nr, nc) not in visited and
                    heights[nr][nc] >= heights[r][c]):  # reversed condition
                    
                    dfs(nr, nc, visited)
        
        # Start DFS from Pacific borders
        for c in range(cols):
            dfs(0, c, pacific)           # top row
            dfs(rows-1, c, atlantic)     # bottom row
        
        for r in range(rows):
            dfs(r, 0, pacific)           # left column
            dfs(r, cols-1, atlantic)     # right column
        
        # Intersection
        return list(pacific & atlantic)
