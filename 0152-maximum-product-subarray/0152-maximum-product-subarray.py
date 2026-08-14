class Solution(object):
    def maxProduct(self, nums):
        maxi=float('-inf')
        # summ=1
        # neg=1
        pre,suff=1,1
        n=len(nums)
        for i in range(n):
            if pre==0:
                pre=1
            if suff==0:
                suff=1
            pre*=nums[i]
            suff*=nums[n-i-1]
            maxi1=max(pre,suff)   
            maxi=max(maxi,maxi1)
        return maxi