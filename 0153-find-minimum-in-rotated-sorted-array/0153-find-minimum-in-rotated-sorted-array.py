class Solution(object):
    def findMin(self, nums):
        sz=len(nums)
        left,right=0,sz-1
        
        while left<=right:
            mid=(left+right)/2
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[left]:
                right = mid
            else:
                return nums[left]

        