class Solution(object):
    def missingNumber(self, nums):
        i = 0
        sz=len(nums)
        while i < sz:
            correct = nums[i]

            if nums[i]<sz and nums[i] != nums[correct]:
                nums[i], nums[correct] = nums[correct], nums[i]
            else:
                i += 1

        for i in range(len(nums)):
            if nums[i] != i:
                return i

        return len(nums)