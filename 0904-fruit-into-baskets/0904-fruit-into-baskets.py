class Solution(object):
    def totalFruit(self, fruits):
        ans = 0
        count = 0
        a = {}
        left = 0
        for i in range(len(fruits)):
            if fruits[i] in a:
                a[fruits[i]] += 1
            elif count < 2:
                a[fruits[i]] = 1
                count += 1
            else:
                while count == 2:
                    a[fruits[left]] -= 1

                    if a[fruits[left]] == 0:
                        del a[fruits[left]]
                        count -= 1

                    left += 1

                a[fruits[i]] = 1
                count += 1

            ans = max(ans, i - left + 1)

        return ans