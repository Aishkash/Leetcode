class Solution(object):
    def dailyTemperatures(self, temperatures):
        sz = len(temperatures)
        ans = [0] * sz
        stack = []

        for i in range(sz-1, -1, -1):

            while stack and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()

            if stack:
                ans[i] = stack[-1] - i

            stack.append(i)

        return ans