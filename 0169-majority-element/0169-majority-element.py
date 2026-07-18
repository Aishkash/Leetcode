class Solution(object):
    def majorityElement(self, nums):
        nums.sort()
        sz=len(nums)
        mid=sz/2
        k=1
        for i in range(sz-1):
            if nums[i]==nums[i+1]:
                k+=1
                if k>mid:
                    return nums[i]
            else:
                k=1
        return nums[0]