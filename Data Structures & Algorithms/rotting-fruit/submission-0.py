class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        row_size = len(grid)
        col_size = len(grid[0])
        queue = deque()
        seen = set()
        good_count = 0
        for r in range(row_size):
            for c in range(col_size):
                if grid[r][c] == 2:
                    queue.append((r,c))
                    seen.add((r,c))
                if grid[r][c] == 1:
                    good_count += 1

        minutes = 0
        movements = [[1,0], [-1,0], [0,1], [0,-1]]

        """
        On the final round when the last fresh orange is infected, 
        the newly rotten oranges still enter the queue. The loop runs one extra 
        time just to pop them and discover no neighbors can be infected, 
        adding an unintended minute. So we do good_count > 0 in while loop
        """
        while queue and good_count > 0 :
            minutes += 1
            queue_len = len(queue)
            for i in range(queue_len):
                row, col = queue.popleft()
                for movement in movements:
                    new_row = row + movement[0]
                    new_col = col + movement[1]
                    if min(new_row, new_col) < 0 or new_row == row_size or \
                    new_col == col_size or (new_row, new_col) in seen or \
                    grid[new_row][new_col] != 1:
                        continue
                    else:
                        queue.append((new_row, new_col))
                        seen.add((new_row, new_col))
                        good_count -= 1
        if good_count > 0:
            return -1
        return minutes


         


        