from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid is None:
            return -1
        
        neighbours = deque()
        visited =set()
        rows, cols = len(grid), len(grid[0])

        if grid[0][0] == 0:
            neighbours.append(((0,0),1))
            visited.add((0,0))
        
        directions = []
        for i in [-1, 0 , 1]:
            for j in [-1, 0 , 1]:
                if not (i == 0 and j==0):
                    directions.append((i,j))


        while neighbours:
            (r,c), dist = neighbours.popleft()

            if (r,c) == ((rows-1) , (cols-1)):
                return dist 
            
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc 

                neighbor = (nr, nc)

                if neighbor not in visited and 0<=nr < rows and 0<=nc < cols and grid[nr][nc] != 1:
                    visited.add(neighbor)
                    neighbours.append((neighbor, dist+1))
        return -1






        