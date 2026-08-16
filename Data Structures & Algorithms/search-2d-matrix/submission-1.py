class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # First do a binary search on the rows to figure out which row to pick
        # Second do a binary search on the selected row to check the target
        # complexity is O(Log(rows * Columns))

        low = 0
        high = len(matrix) -1
        selected_row = -1

        while low <= high:
            mid = (low + high) // 2

            # check the first and last elements of the mid row if target exists
            mid_first = matrix[mid][0]
            mid_last = matrix[mid][len(matrix[mid]) -1]

            if target < mid_first:
                high = mid -1

            elif target > mid_last:
                low = mid +1

            else:
                selected_row = mid
                break

        # check if we got a valid answer
        if selected_row == -1:
            return False

        low = 0
        high = len(matrix[selected_row]) -1

        while low <= high:
            mid = (low + high) // 2

            if target < matrix[selected_row][mid]:
                high = mid -1

            elif target > matrix[selected_row][mid]:
                low = mid + 1

            else:
                return True

        return False
        

        