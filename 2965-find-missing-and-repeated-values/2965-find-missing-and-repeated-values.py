class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        sz=len(grid)
        way=sz**2
        c={}
    
        for i in range(sz):
            for j in range(sz):
                val= grid[i][j]
                c[val]=c.get(val,0)+1
        a,b=-1,-1
        for i in range(1,way+1):
            if i not in c:
                a=i
            elif c[i]==2:
                b=i


        return [b,a]

