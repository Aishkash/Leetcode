class Solution(object):
    def maxProduct(self, nums):
        ans=float('-inf')
        summ=1
        neg=1
        for i in nums:
            if i == 0:
                ans = max(ans, 0)
                summ = 1
                neg = 1
                continue

            if i < 0:
                summ, neg = neg, summ
            summ = max(i, summ * i)
            neg = min(i, neg * i)
            ans = max(ans, summ)

        return ans