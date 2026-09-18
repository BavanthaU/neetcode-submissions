class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ''
        for i in strs:
            out = out+'encoded'+i
        return out


    def decode(self, s: str) -> List[str]:
        out = s.split('encoded')
        return out[1:]

