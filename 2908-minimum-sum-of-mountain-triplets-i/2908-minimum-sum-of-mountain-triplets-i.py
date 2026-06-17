class Solution(object):
    def minimumSum(self, nums):
        ans = float('inf')
        n = len(nums)

        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                if nums[i] < nums[j]:
                    for k in range(j + 1, n):
                        if nums[k] < nums[j]:
                            ans = min(ans, nums[i] + nums[j] + nums[k])

        return -1 if ans == float('inf') else ans