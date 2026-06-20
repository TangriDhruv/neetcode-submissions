class Solution:

    def encode(self, strs: List[str]) -> str:
        final_s =""
        for s in strs:
            final_s = final_s+s+"|"
        return final_s

    def decode(self, s: str) -> List[str]:
        l = s.split("|")
        return l[:-1]
