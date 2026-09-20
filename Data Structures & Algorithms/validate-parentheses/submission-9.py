class Solution:
    def isValid(self, s: str) -> bool:
        bracket = {')':'(', '}':'{', ']':'['}
        out = []

        for b in s:
            if b in bracket:
                if out:
                    op = out.pop()
                    if bracket[b]!=op:
                        return False
                else:
                    return False
            else:
                out.append(b)
        
        return not out
 



        