from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        freq = {}
        for i in nums:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1

        # sort by value
        freq = sorted(freq.items(), key=lambda item: item[1], reverse=True)

        # put it in dict
        for j in range(k):
            res.append(freq[j][0])
        return res
