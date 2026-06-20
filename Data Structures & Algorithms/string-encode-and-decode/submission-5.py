class Solution:

    def encode(self, strs: List[str]) -> str:
        s= ""
        for str_1 in strs:
            s = s+"#|#"+str_1
        return s

    def decode(self, s: str) -> List[str]:
        l = s.split("#|#")
        return l[1:]


