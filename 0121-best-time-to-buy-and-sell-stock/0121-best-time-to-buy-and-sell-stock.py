class Solution(object):
    def maxProfit(self, prices):
        mini=prices[0]
        maxi=0
        n=len(prices)
        for i in range(1,n):
            if mini<prices[i]:
                maxi=max(maxi,prices[i]-mini)
            else:
                mini=prices[i]
        return maxi