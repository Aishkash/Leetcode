class Solution(object):
    def isValidSudoku(self, board):
        for i in range(9):
            s=set()
            for j in range(9):
                a=board[i][j]
                if a in s:
                    return False
                elif a !='.':
                    s.add(a) 
        for i in range(9):
            s=set()
            for j in range(9):
                a=board[j][i]
                if a in s:
                    return False
                elif a!='.':
                    s.add(a) 

        stars=[(0,0),(0,3),(0,6),
               (3,0),(3,3),(3,6),
               (6,0),(6,3),(6,6)]


        for i,j in stars:
            s=set()
            for row in range(i,i+3):
                for col in range(j,j+3):
                    a=board[row][col]
                    if a in s:
                        return False
                    elif a!='.':
                        s.add(a)
        return True



        