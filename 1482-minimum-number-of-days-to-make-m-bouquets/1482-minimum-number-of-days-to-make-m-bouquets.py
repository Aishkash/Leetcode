class Solution(object):
    def minDays(self, bloomDay, m, k):
        sz = len(bloomDay)

        if sz < m * k:
            return -1

        left = min(bloomDay)
        right = max(bloomDay)

        while left < right:
            mid = (left + right) // 2
            b = 0
            count = 0

            for i in range(sz):
                if bloomDay[i] <= mid:
                    count += 1

                    if count == k:
                        b += 1
                        count = 0
                else:
                    count = 0

            if b >= m:
                right = mid
            else:
                left = mid + 1

        return left