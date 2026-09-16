class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        seen = set()
        queue = deque()
        row_size = len(grid)
        col_size = len(grid[0])
        if grid[0][0] == 1 or grid[row_size-1][col_size-1] == 1:
            return -1
        
        # add row, col, length to queue
        queue.append((0,0,1))

        while queue:
            row, col, path_length = queue.popleft()

            # Check if we reached the end
            if row == row_size -1 and col == col_size -1:
                return path_length

            seen.add((row, col))
            possible_movements = [[1,0], [1,1], [-1,0], [0,1], [0,-1], [-1,-1], [1,-1], [-1,1]]
            path_length += 1
            for movement in possible_movements:
                new_row = row + movement[0]
                new_col = col + movement[1]
                # check for valid movements:
                if min(new_row, new_col) < 0 or new_row == row_size or \
                new_col == col_size or (new_row, new_col) in seen or \
                grid[new_row][new_col] == 1:
                    continue
                else:
                    queue.append((new_row, new_col, path_length))

        # No valid path exists
        return -1

        
        