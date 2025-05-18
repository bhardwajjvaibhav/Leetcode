class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row,col=len(grid),len(grid[0])
        visited=set()
        island_count=0

        def dfs(r,c):
            if (r<0 or r>=row or c<0 or c>=col or grid[r][c]=='0' or (r,c) in visited):
                return
            visited.add((r,c))
            dfs(r,c+1)
            dfs(r,c-1)
            dfs(r-1,c)
            dfs(r+1,c)

        for r in range(row):
            for c in range(col):
                if (grid[r][c]=='1' and (r,c) not in visited):
                    dfs(r,c)
                    island_count+=1
        return island_count