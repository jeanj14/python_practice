
class Solution:
    def twoSum(self, nums: list[int], target: int):
        seen = {}

        for i, num in enumerate(nums):
            if target - num in seen:
                return(seen[target - num], i)
            elif num not in seen:
                seen[num] = i
