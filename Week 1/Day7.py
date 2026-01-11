from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set) #box_key will be (r//3, c//3)

        for r in range(9):
            for c in range(9):
                val = board[r][c]

                if val == ".":
                    #if the current value of board[r][c]=="." we move on to the next number
                    continue 
                
                if (val in rows[r] or val in cols[c] or val in boxes[(r//3, c//3)]):
                    # if the value is in the current column, the current row or the current 3x3 board, return false
                    return False

                #else add the value to the hashmaps, clearing the value and granting entrance
                rows[r].add(val)
                cols[c].add(val)
                boxes[(r//3, c//3)].add(val)

        return True