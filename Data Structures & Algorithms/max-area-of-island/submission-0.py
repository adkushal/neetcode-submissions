class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        area = 0
        row_size = len(grid)
        col_size = len(grid[0])

        def dfs(row, col, seen):
            nonlocal area
            # check base cases
            if min(row, col) < 0 or \
            row == row_size or col == col_size or \
            grid[row][col] == 0 or (row,col) in seen:
                return

            area += 1
            seen.add((row,col))

            dfs(row+1, col, seen)
            dfs(row-1, col, seen)
            dfs(row, col+1, seen)
            dfs(row, col-1, seen)

        seen = set()
        for r in range(row_size):
            for c in range(col_size):
                    dfs(r,c,seen)
                    max_area = max(max_area, area)
                    area = 0

        return max_area

        