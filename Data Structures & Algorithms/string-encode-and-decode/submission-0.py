class Solution:

    def encode(self, strs: List[str]) -> str:
        line = ""
        for s in strs:
            line = line + s +"|"
        print(line)
        return line


    def decode(self, s: str) -> List[str]:
        strs = s.split("|")
        strs = strs[:len(strs)-1]
        print(strs[:len(strs)-1])
        return strs
