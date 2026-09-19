class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ''
        for i in strs:
            out = out+'|--#--|'+i
        return out


    def decode(self, s: str) -> List[str]:
        out = s.split('|--#--|')
        return out[1:]

