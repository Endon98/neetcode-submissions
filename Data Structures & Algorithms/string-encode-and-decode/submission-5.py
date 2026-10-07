class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return "\r"
        if len(strs) == 1:
            return "\t" if strs[0] == "" else strs[0]
        return "\n".join(e for e in strs)

    def decode(self, s: str) -> List[str]:
        if s == "\r":
            return []
        if s == "\t":
            return [""]
        return s.split("\n")
