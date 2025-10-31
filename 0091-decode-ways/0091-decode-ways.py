class Solution(object):
    def numDecodings(self, s):
        if not s or s[0] == '0':
            return 0

        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1  # empty string
        dp[1] = 1  # first char (already checked it's not '0')

        for i in range(2, n + 1):
            one = int(s[i - 1:i])      # last 1 digit
            two = int(s[i - 2:i])      # last 2 digits

            if 1 <= one <= 9:
                dp[i] += dp[i - 1]
            if 10 <= two <= 26:
                dp[i] += dp[i - 2]

        return dp[n]