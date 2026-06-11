class Solution(object):
    def findMin(self, nums):
        a=len(nums)
        l=0
        r=a-1
        
        while l<=r:
            mid=(l+r)/2
            if nums[mid]>nums[r]:
                l=mid+1
            elif nums[mid]<nums[l]:
                r=mid
            else:
                return nums[l]