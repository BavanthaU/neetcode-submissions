from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows = len(grid)
        cols = len(grid[0])
        islands = 0

        def bfs(r, c):
            # create queue
            queue = deque([(r, c)])
            grid[r][c] = "0"

            while queue:
                # pop current cell
                q = queue.popleft()
                directions = [(1,0), (-1,0), (0,1), (0,-1)]

                for dr, dc in directions:
                    nr = q[0]+dr
                    nc = q[1]+dc

                    if (
                        0<=nr<rows and 0<= nc < cols
                        and grid[nr][nc] =="1"
                    ):
                        grid[nr][nc] = "0"
                        queue.append((nr, nc))
                        # visit and enqueue

        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == "1":
                    islands += 1
                    bfs(r, c)

        return islands