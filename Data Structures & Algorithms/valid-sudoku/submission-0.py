class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # We use separate hash maps for rows, columns, and squares.
        # for squares/blocks we use the formula :
        # index = (row//3 * 3) + col//3
        row_set = defaultdict(set)
        col_set = defaultdict(set)
        block_set = defaultdict(set)

        for row_index, row in enumerate(board):
            for col_index, value in enumerate(row):
                if value == ".":
                    continue

                num = int(value)

                # check row integrity:
                if num in row_set[row_index]:
                    return False
                else:
                    row_set[row_index].add(num)

                # check col integrity:
                if num in col_set[col_index]:
                    return False
                else:
                    col_set[col_index].add(num)

                # check block integrity
                block_index = (row_index // 3 * 3) + col_index // 3
                if num in block_set[block_index]:
                    return False
                else:
                    block_set[block_index].add(num)

        return True
                

        


        