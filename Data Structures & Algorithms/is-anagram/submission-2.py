class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # freq
        freq = {}
        for char in s:
            freq[char] = 1 if char not in freq else freq[char]+1
        print(freq)
        # sub from freq map
        for char in t:
            if char not in freq:
                return False
            elif freq[char] == 0:
                return False
            freq[char] -= 1
        print(freq)
        for i in freq.values():
            if i !=0:
                return False
            
        return True 