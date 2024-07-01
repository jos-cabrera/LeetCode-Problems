# Problem 36 - Valid Sudoku
# https://leetcode.com/problems/valid-sudoku

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        for i in range(0, 9):
            rows = set()
            columns = set()
            
            
            for j in range(0, 9):
                if board[i][j] != "." and board[i][j] in rows:
                    return False
                else:
                    rows.add(board[i][j])
                    
                
                if board[j][i] != "." and board[j][i] in columns:
                    return False
                else:
                    columns.add(board[j][i])

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                rows = set()
                columns = set()
                for k in range(i, i+3):
                    for l in range(j, j+3):
                        if board[k][l] != "." and board[k][l] in rows:
                            return False
                        else:
                            rows.add(board[k][l])
                        
                        if board[l][k] != "." and board[l][k] in columns:
                            return False
                        else:
                            columns.add(board[l][k])
        return True