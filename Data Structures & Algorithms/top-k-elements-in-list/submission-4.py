from typing import List
from collections import Counter
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = list(Counter(nums).items())
        heap = []
        for f in freq:
            heapq.heappush_max(heap, (f[1], f[0]))
        return [heapq.heappop_max(heap)[1] for _ in range(k)]
