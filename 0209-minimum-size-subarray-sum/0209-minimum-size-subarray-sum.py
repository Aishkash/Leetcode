class Solution(object):
    def minSubArrayLen(self, target, nums):
        sz=len(nums)
        l=0
        total=0
        ans=float('inf')
        for r in range(sz):
            total+=nums[r]

            while total >= target:
                ans = min(ans, (r - l) + 1)
                total -= nums[l]
                l += 1
        if ans==float('inf'):
            return 0
        else:    
            return ans