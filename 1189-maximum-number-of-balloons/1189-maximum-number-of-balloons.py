class Solution(object):
    def maxNumberOfBalloons(self, text):
        a = {}

        for i in text:
            a[i] = a.get(i, 0) + 1

        return min(
            a.get('b', 0),
            a.get('a', 0),
            a.get('l', 0) // 2,
            a.get('o', 0) // 2,
            a.get('n', 0)
        )