class Solution(object):
    def findDuplicates(self, nums):
        i=0
        sz=len(nums)
      
        while i < sz:
            correct = nums[i]-1

            if nums[i] != nums[correct]:
                nums[i], nums[correct] = nums[correct], nums[i]
            else:
                i += 1

        ans = []
        for i in range(sz):
            if nums[i] != i + 1:
                ans.append(nums[i])
        return ans