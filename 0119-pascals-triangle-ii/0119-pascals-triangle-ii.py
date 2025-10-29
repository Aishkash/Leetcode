class Solution(object):
    def getRow(self, rowIndex):
        row = [1]
        for _ in range(rowIndex):
            # create next row using zip to sum pairs
            row = [1] + [a + b for a, b in zip(row, row[1:])] + [1]
        return row
        