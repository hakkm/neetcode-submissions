from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        frozens = {}
        # O(mn)
        for st in strs:
            fx = self._hash(st)
            if fx not in frozens:
                frozens[fx] = [st]
            else:
                frozens[fx].append(st)
        return list(frozens.values())

    def _hash(self, st):
        """same freq => same hash"""
        freq = defaultdict(int)
        # O(n)
        for i in st:
            freq[i] += 1

        res = frozenset(f"{k}{v}" for k, v in freq.items())
        return res
