class Solution(object):
    def candy(self, ratings):
        n=len(ratings)
        a=[1]*n
        for i in range(1,n):
            if ratings[i]>ratings[i-1]:
                a[i]=a[i-1]+1
        for i in range(n-2,-1,-1):
            if ratings[i]>ratings[i+1]:
                k=a[i+1]+1
                if k>a[i]:
                    a[i]=k
        return sum(a)