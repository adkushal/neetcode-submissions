class Solution:
    # We rely on color values rather than seen set to avoid loops
    # and backtrack
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        def dfs(grid, row, col, src_pixel, dest_pixel):
            row_count = len(grid)
            col_count = len(grid[0])

            # Check various cases that we should avoid
            if min(row, col) < 0 or \
               row == row_count or col == col_count or \
               grid[row][col] != src_pixel:
                    return

            # color the current node
            grid[row][col] = dest_pixel

            # travel all four directions
            dfs(grid, row+1, col, src_pixel, dest_pixel)
            dfs(grid, row-1, col, src_pixel, dest_pixel)
            dfs(grid, row, col+1, src_pixel, dest_pixel)
            dfs(grid, row, col-1, src_pixel, dest_pixel)

            return

        src_pixel = image[sr][sc]
        # IMP: Check that the src and dest pixel arent the same, or else
        # DFS continuously bounces back and forth between row + 1 and row - 1
        if src_pixel == color:
            return image
        dfs(image, sr, sc, src_pixel, color)
        return image



        