class Solution(object):
    def minEatingSpeed(self, piles, h):
        sz = len(piles)
        right = max(piles)
        left = 1

        while left < right:
            mid = (left + right) // 2
            a = 0

            for i in piles:
                a += (i + mid - 1) // mid

            if a > h:
                left = mid + 1
            else:
                right = mid

        return left