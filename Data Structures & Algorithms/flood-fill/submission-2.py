class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        row = len(image)
        col = len(image[0])
        seen = set()
        direction = [[-1,0],[0,1],[1,0],[0,-1]]
        def dfs(x,y):
            if x<0 or x>=row or y<0 or y>=col or image[x][y] != c or (x,y) in seen:
                return
            seen.add((x,y))
            image[x][y] = color
            for dx,dy in direction:
                dfs(x+dx,y+dy)
        c = image[sr][sc]
        dfs(sr,sc)
        return image
        