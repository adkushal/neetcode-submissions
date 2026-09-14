class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        def dfs(grid, row, col, seen, src_pixel, dest_pixel):
            row_count = len(grid)
            col_count = len(grid[0])

            # Check various cases that we should avoid
            if min(row, col) < 0 or \
               row == row_count or col == col_count or \
               (row,col) in seen or \
               grid[row][col] != src_pixel:
                    return

            # visit the current node
            seen.add((row, col))

            # color the current node
            grid[row][col] = dest_pixel

            # travel all four directions
            dfs(grid, row+1, col, seen, src_pixel, dest_pixel)
            dfs(grid, row-1, col, seen, src_pixel, dest_pixel)
            dfs(grid, row, col+1, seen, src_pixel, dest_pixel)
            dfs(grid, row, col-1, seen, src_pixel, dest_pixel)

            # backtrack and unvisit the node
            seen.remove((row, col))
            return

        src_pixel = image[sr][sc]
        dfs(image, sr, sc, set(), src_pixel, color)
        return image



        