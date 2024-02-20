class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        size_of_board=9
        digits={str(i) for i in range(1,10)}
        rows=[set() for _ in range(size_of_board)]
        cols=[set() for _ in range(size_of_board)]
        boxes=[set() for _ in range(size_of_board)]

        for r in range(size_of_board):
            for c in range(size_of_board):
                digit=board[r][c]
                if digit =='.':
                    continue
                if digit not in digits:
                    return False
                box =(size_of_board//3)*(r//(size_of_board//3))+(c//(size_of_board//3))
                if digit in rows[r] or digit in cols[c] or digit in boxes[box]:
                    return False
                rows[r].add(digit)
                cols[c].add(digit)
                boxes[box].add(digit)
        return True
        
        