class Solution(object):
    def maxSubArray(self, nums):
        ans=float('-inf')
        summ=0
        for i in nums:
            summ+=i
            ans=max(ans,summ)
            if summ<0:
                summ=0
            
      
        return ans
        