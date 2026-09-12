class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapper = {}
        for index, item in enumerate(nums):
            mapper[item] = index
        for i,v in enumerate(nums):
            if target - v in mapper and mapper[target -v] != i:
                return [i, mapper[target- v]]