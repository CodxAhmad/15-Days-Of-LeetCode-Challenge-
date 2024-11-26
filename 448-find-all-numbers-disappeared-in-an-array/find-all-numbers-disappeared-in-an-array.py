class Solution(object):
    def findDisappearedNumbers(self, nums):
        nums_set = set(nums)
        x = len(nums)
        lis = [i for i in range(1, x + 1) if i not in nums_set]
        return lis
