class Solution(object):
    def pivotIndex(self, nums):
        a=sum(nums)
        sz=len(nums)
        left,right=0,0
        for i in range(0,sz):
            right=a-left-nums[i]
            if left==right:
                return i
            left+=nums[i]
        return -1