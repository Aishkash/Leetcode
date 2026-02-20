class Solution(object):
    def maxProfit(self, prices):
        mini=prices[0]
        maxi=0
        for i in range(1,len(prices)):
            maxi=max(maxi,prices[i]-mini)
            if prices[i]<mini:
                mini=prices[i]

        return maxi