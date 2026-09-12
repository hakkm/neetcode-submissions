class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums_set = set(nums) 
        maxi = 1
        i = 0
        for i in nums:
            # this is the starting point.
            if i - 1 not in nums_set:
                j = i
                maxi_tmp = 1
                while j + 1 in nums_set:
                    maxi_tmp += 1
                    j += 1
                maxi = max(maxi, maxi_tmp)
        return maxi