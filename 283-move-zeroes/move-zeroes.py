class Solution(object):
    def moveZeroes(self, nums):
        index = 0
        for i in range(len(nums)):
            if nums[i]!=0 and index!=i:
                nums[index] = nums[i]
                index+=1
                nums[i] = 0
            if index==i and nums[i]!=0:
                index+=1