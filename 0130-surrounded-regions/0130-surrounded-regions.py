class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.

        """
        if not board or not board[0]:
            return
        row,col=len(board),len(board[0])
        visited=set()

        def dfs(r,c):
            if (r < 0 or r >= row or c < 0 or c >= col or
                board[r][c] == 'X' or (r, c) in visited):
                return
            visited.add((r, c))
            
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for c in range(col):
            for r in [0,row-1]:
                if board[r][c] =='O' and (r,c) not in visited:
                    dfs(r,c)
        
        for r in range(row):
            for c in [0,col-1]:
                if board[r][c] =='O' and (r,c) not in visited:
                    dfs(r,c)

        for r in range(row):
            for c in range(col):
                if board[r][c]=='O' and (r,c) not in visited:
                    board[r][c]='X'
        