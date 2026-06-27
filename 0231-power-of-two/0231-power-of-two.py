class Solution(object):
    def isPowerOfTwo(self, n):
        if n<1:
            return False
        if n==8:
            return True
        sqr=int(n**0.5)
        
        for i in range(sqr,-1,-1):
            k=2**i
            if k==n:
                return True
            if k<n:
                return False   

        