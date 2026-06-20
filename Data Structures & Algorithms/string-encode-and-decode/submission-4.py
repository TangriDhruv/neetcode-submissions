class Solution:

    def encode(self, strs: List[str]) -> str:
        new_str = ""
        for s in strs:
            new_str = new_str + "#|#" + s
        return new_str


    def decode(self, s: str) -> List[str]:
        strs = s.split("#|#")
        return strs[1:]

