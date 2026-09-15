class Solution:
    def shipWithinDays(self, weights, days):
        low = max(weights)
        high = sum(weights)

        while low < high:
            capacity = (low + high) // 2

            current = 0
            needed_days = 1

            for weight in weights:
                if current + weight > capacity:
                    needed_days += 1
                    current = 0

                current += weight

            if needed_days <= days:
                high = capacity
            else:
                low = capacity + 1

        return low