class Solution:
    def isValid(self, s: str) -> bool:
        bracket = {')':'(', '}':'{', ']':'['}
        out = []

        for b in s:
            if b in bracket:
                if not out or bracket[b]!=out.pop():
                    return False
            else:
                out.append(b)
        
        return not out
 



        