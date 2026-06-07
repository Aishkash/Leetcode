class Solution(object):
    def maxProfit(self, prices):
        n=len(prices)
        summ=0
        for i in range(1,n):
            if prices[i]>prices[i-1]:
                k=prices[i]-prices[i-1]
                summ+=k
        return summ

        