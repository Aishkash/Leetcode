class Solution(object):
    def sortColors(self, nums):
        sz=len(nums)-1
        for j in range(sz, -1, -1):
            i = j
            if nums[j] != 2:
                i -= 1
                while i >= 0 and nums[i] != 2:
                    i -= 1
                if i >= 0:
                    nums[i], nums[j] = nums[j], nums[i]

        for j in range(0, sz + 1):
            i = j
            if nums[j] != 0:
                i += 1
                while i <= sz and nums[i] != 0:
                    i += 1
                if i <= sz:

                    nums[i], nums[j] = nums[j], nums[i]