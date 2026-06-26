class Solution(object):
    def maxSubArray(self, nums):
        a=float('-inf')
        maxi=0
        for i in nums:
            maxi+=i
            if maxi>a:
                a=maxi
            if maxi<0:
                maxi=0
        return a
        