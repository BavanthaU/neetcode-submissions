class Solution:

    def encode(self, strs: List[str]) -> str:
        out = []
        for i in strs:
            tmp = str(len(i))+'#'+ i
            out.append(tmp)
        return ''.join(out)


    def decode(self, s: str) -> List[str]:
        left = 0
        i=0
        out =[]

        while left < len(s):
            while s[left+i].isnumeric():
                i+=1
            if s[left:left+i].isnumeric() and s[left+i]=='#':
                end_str = left + int(s[left:left+i]) + i +1
                out.append(s[left+i+1:end_str])
                left = end_str
            else:
                out.clear()
                out.append("Received Message is corrupted")
                break
            i=0
        return out




