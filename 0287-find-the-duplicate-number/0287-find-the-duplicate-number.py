class Solution(object):
    def findDuplicate(self, nums):
        i=0
        sz=len(nums)
        while i < sz:
            correct = nums[i]

            if nums[i]<sz and nums[i] != nums[correct-1]:
                nums[i], nums[correct-1] = nums[correct-1], nums[i]
            else:
                i += 1

        for i in range(sz):
            if nums[i] != i+1:
                return nums[i]
            

        