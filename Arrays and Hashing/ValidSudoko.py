import collections

class Solution:
    #Hashset for each row and each column to identify duplicates
    #also use a hashset for each 3x3 grid
    #Lets say grid is 0-9 on each side. we also have nine 3x3 grids.
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Hash set for columsn, rows, and 3x3 subgrids
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)  #key = (r/3, c/3)

        #go through the board cell by cell
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".": #skip if empty
                    continue
                #if found duplicate reject
                if ( board[r][c] in rows[r] #duplicate in row
                    or board[r][c] in cols[c] #duplicate in column
                    or board[r][c] in squares[(r // 3, c // 3)]): #duplicate in subgrid
                    return False
                #add current value to its appropriate column, row and subgrid
                cols[c].add(board[r][c]) 
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
        #If no duplicates found, we can return true.
        return True