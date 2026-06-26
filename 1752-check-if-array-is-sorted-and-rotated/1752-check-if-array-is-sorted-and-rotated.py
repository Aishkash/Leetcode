class Solution(object):
    def check(self, nums):
        sz=len(nums)
        a=0
        for i in range(sz-1):
            if nums[i]>nums[i+1]:
                a+=1
        if nums[sz-1]>nums[0]:
            a+=1
        return a<=1
        