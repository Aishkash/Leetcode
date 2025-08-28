class Solution(object):
    def maxProduct(self, nums):
        sz=len(nums)
        if not nums:
            return 0
        
        pre=1
        suf=1
        max_prod=float("-inf")
        
        for i in range(sz):
            pre *= nums[i]
            suf *= nums[sz-1-i]
            max_prod = max(max_prod, pre, suf)
            
            if nums[i] == 0:
                pre = 1
            if nums[sz-1-i] == 0:
                suf = 1

        return max_prod