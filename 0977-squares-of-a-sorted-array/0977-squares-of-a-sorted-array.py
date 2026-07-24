class Solution(object):
    def sortedSquares(self, nums):
        sz=len(nums)
        a=0
        for i in range(sz):
            nums[i]=nums[i]**2
        return sorted(nums)
        
        
        