class Solution(object):
    def removeDuplicates(self, nums):
        sz=len(nums)
        l,r=0,0
        while r<sz:
            k=1
            while r+1<sz and nums[r]==nums[r+1]:
                r+=1
                k+=1
            s=min(2,k)
            for i in range(s):
                nums[l]=nums[r]
                l+=1
            r+=1
        return l
