class Solution:
    def isValid(self, s: str) -> bool:
        bracket = {')':'(', '}':'{', ']':'['}
        out = []

        for b in s:
            if b in bracket:
                if out:
                    if bracket[b]!=out.pop():
                        return False
                else:
                    return False
            else:
                out.append(b)
        
        return not out
 



        