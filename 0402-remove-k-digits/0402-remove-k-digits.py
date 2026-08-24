class Solution(object):
    def removeKdigits(self, num, k):
        sz = len(num)

        if sz == k:
            return "0"

        stack = []

        for i in num:
            while stack and k > 0 and stack[-1] > i:
                stack.pop()
                k -= 1

            stack.append(i)

        while k > 0:
            stack.pop()
            k -= 1

        return ''.join(stack).lstrip('0') or '0'