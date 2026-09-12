from collections import deque
from typing import List

class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        # dist_sum[r][c] = sum of distances from all buildings
        dist_sum = [[0] * cols for _ in range(rows)]

        # reach[r][c] = number of buildings that can reach this cell
        reach = [[0] * cols for _ in range(rows)]

        buildings = 0

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        def bfs(start_r, start_c):
            visited = [[False] * cols for _ in range(rows)]
            queue = deque([(start_r, start_c, 0)])
            visited[start_r][start_c] = True

            while queue:
                r, c, dist = queue.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if (
                        0 <= nr < rows
                        and 0 <= nc < cols
                        and not visited[nr][nc]
                        and grid[nr][nc] == 0
                    ):
                        visited[nr][nc] = True

                        dist_sum[nr][nc] += dist + 1
                        reach[nr][nc] += 1

                        queue.append((nr, nc, dist + 1))

        # Run BFS starting from every building
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    buildings += 1
                    bfs(r, c)

        answer = float("inf")

        # Find an empty cell reachable from every building
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0 and reach[r][c] == buildings:
                    answer = min(answer, dist_sum[r][c])

        return -1 if answer == float("inf") else answer