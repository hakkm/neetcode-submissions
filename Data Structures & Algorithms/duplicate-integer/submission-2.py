class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        print(len(nums))
        return len(nums) != len(set(nums))