class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            # two sum problem of the rest
            l = i + 1
            r = len(nums) - 1

            while l + 1 <= r:
                if nums[i] + nums[l] + nums[r] == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l != len(nums) - 1 and nums[l] == nums[l - 1]:
                        l += 1
                elif nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                    while r > 0 and nums[r + 1] == nums[r]:
                        r -= 1
                else:
                    l += 1
                    while l < len(nums) - 1 and nums[l] == nums[l - 1]:
                        l += 1
        return res


