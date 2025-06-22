'''
    Time Complexity: O(n*2^n)
    Space Complexity: O(n)
'''
class Solution:
    def __init__(self):
        self.result = 0

    def countArrangement(self, n: int) -> int:
        nums = [i + 1 for i in range(n)]
        self.helper(nums, 0, set())
        return self.result

    def helper(self, nums, pos, hashset):
        # base case
        if pos == len(nums):
            self.result += 1
            return

        # logic
        for i in range(len(nums)):
            if nums[i] not in hashset:
                if nums[i] % (pos + 1) == 0 or (pos + 1) % nums[i] == 0:
                    hashset.add(nums[i])
                    self.helper(nums, pos + 1, hashset)
                    hashset.remove(nums[i])
