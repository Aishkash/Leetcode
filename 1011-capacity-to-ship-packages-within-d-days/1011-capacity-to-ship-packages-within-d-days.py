class Solution(object):
    def shipWithinDays(self, weights, days):
        sz=len(weights)
        left=max(weights)
        right=sum(weights)
        while left<right:
            mid=(left+right)//2

            a=0
            summ=1
            for i in weights:
                if a+i<=mid:
                    a+=i
                else:
                    summ+=1
                    a=i
            if summ<=days:
                right=mid
            else:
                left=mid+1
        return left