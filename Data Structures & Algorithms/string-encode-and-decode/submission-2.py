class Solution:
    separator = "|||||||"
    nothing = "////////////////"
    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return self.nothing
        print(self.separator.join(strs))
        return self.separator.join(strs)

    def decode(self, s: str) -> List[str]:
        if s == self.nothing:
            return []
        return s.split(self.separator)
