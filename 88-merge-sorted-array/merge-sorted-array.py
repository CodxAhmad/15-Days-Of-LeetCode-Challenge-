class Solution(object):
    def merge(self, nums1, m, nums2, n):
        x = 0
        for i in range(m, len(nums1)):
            nums1[i] = nums2[x]
            x+=1
        nums1.sort()