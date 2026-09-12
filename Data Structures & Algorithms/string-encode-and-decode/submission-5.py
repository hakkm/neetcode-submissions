class Solution:

    def encode(self, strs: List[str]) -> str:
        d = ""
        for s in strs:
            d += f"{len(s)}#{s}"
        # print(d)
        return d

    def decode(self, s: str) -> List[str]:
        print(s)
        res = []
        while True:
            if len(s) <= 0:
                break
            # identify the location of #
            loc_of_hash = 0
            for i in s:
                if i == "#":
                    break
                loc_of_hash += 1
            number = s[0:loc_of_hash]
            print(number)
            number = int(number)
            offset = loc_of_hash+1
            res.append(s[offset:number+offset])
            s = s[number+offset:]
        print(res)
        return res


"""
# decode
 01234567890
"4#neet3##co"
take 4#
read 4 chars 
    append neet
remove neet

take 3#
read 3 chars
    append #co
remove #co

repeat until len(s) <= 0

# code 
res = []
while True:
    if len(s) <= 0:
        return []
    number = int(s[0])
    res.append(s[2:number+2])
    s = s[number+2:]
"""
