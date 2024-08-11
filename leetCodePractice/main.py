class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        x = 0
        y = 0
        while (x<len(nums)):
            while(y<len(nums)):
                if nums[x]+nums[y]!=target:
                    y+=1
                else:
                    print(f"The sum of {nums[x]} and {nums[y]} is {target}")
                    break
            x+=1


numlist = [2, 2, 3, 4]
S = Solution()
S.twoSum(numlist, 4)