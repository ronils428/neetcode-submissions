class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # init 3 dictionaries for each row, col and square
        rows = defaultdict(set)
        cols = defaultdict(set)
        squs = defaultdict(set)

        for r in range(9):
            for c in range(9):
                # skip cells that don't have a number
                if board[r][c] == ".":
                    continue

                # check if number already in row, col or square
                if (board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squs[(r // 3, c // 3)]):
                    return False

                # otherwise add to dictionaries
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squs[(r//3, c//3)].add(board[r][c])

        return True