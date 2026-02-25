class Solution(object):
    def maxSubArray(self, nums):
        a=0
        maxi=float('-inf')
        for i in nums:
            a+=i
            maxi=max(a,maxi)
            if a<0:
                a=0
        return maxi