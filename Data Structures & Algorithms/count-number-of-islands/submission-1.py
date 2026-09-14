class Solution:
    # Each time we visit a node with land (1), mark it with (0)
    # If not allowed to update grid, we can use a set seen to track (row,col) visited
    def numIslands(self, grid: List[List[str]]) -> int:
        row_size = len(grid)
        col_size = len(grid[0])

        def dfs(row, col):
            # Check base bases to return
            if min(row, col) < 0 or row == row_size or \
            col == col_size or grid[row][col] == '0' or (row,col) in seen:
                return

            # Visit current node
            seen.add((row,col))

            # Visit all the adjacent nodes
            dfs(row+1, col)
            dfs(row-1, col)
            dfs(row, col+1)
            dfs(row, col-1)

        num_inslands = 0
        seen = set()
        for row in range(row_size):
            for col in range(col_size):
                if (row,col) not in seen and grid[row][col] == '1':
                    dfs(row, col)
                    num_inslands += 1

        return num_inslands
            



        