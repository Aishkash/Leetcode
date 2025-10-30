class Solution(object):
    def canJump(self, nums):
        n_len = len(nums)

        # Case 1: single element (even if 0) → you're already at the end
        if n_len == 1:
            return True

        # Case 2: no zeros → always reachable
        if 0 not in nums:
            return True

        # Case 3: first element is 0 but not the only one → stuck immediately
        if nums[0] == 0:
            return False

        # Collect indices of zeros
        k = [i for i, val in enumerate(nums) if val == 0]

        # Case 4: single zero at last index → fine, you can already reach the end
        if len(k) == 1 and k[0] == n_len - 1:
            return True

        # Case 5: zeros in the middle — check if each can be jumped over
        for zero_index in k:
            if zero_index == n_len - 1:  # last zero already handled above
                continue
            can_jump_over = False
            for j in range(zero_index - 1, -1, -1):
                if nums[j] > (zero_index - j):
                    can_jump_over = True
                    break
            if not can_jump_over:
                return False

        return True