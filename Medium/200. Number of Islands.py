from collections import deque
#BFS
class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def bfs(r, c):
            que = deque()
            visited.add((r,c))
            que.append((r,c))

            while que:
                #regular pop() would pop the most recent for dfs
                row, col = que.popleft()

                # directions right left above below as [dRow, dCol]
                directions = [[1,0], [-1,0], [0, 1], [0,-1]]

                for dRow, dCol in directions:
                    r, c = row + dRow, col + dCol

                    if((r) in range (rows) and
                       (c) in range(cols) and
                       grid[r][c] == "1" and
                       (r, c) not in visited):

                        que.append((r, c))
                        visited.add((r, c))

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in visited:
                    bfs(row,col)
                    islands += 1

        return islands
