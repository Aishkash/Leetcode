class Solution(object):
    def tribonacci(self, n):
        a,b,c=0,1,1
        if n==0:
            return 0
        elif n==1 or n==2:
            return 1

        for i in range(n-2):
            k=a+b+c
            a=b
            b=c
            c=k
        return k    
            




        # for i in range(n-3,n):

        