class Solution(object):
    def splitArray(self, nums, k):
        left = max(nums)
        right = sum(nums)

        while left < right:
            mid = (left + right) // 2

            curr = 0
            parts = 1

            for x in nums:
                if curr + x <= mid:
                    curr += x
                else:
                    parts += 1
                    curr = x

            if parts <= k:
                right = mid
            else:
                left = mid + 1

        return left