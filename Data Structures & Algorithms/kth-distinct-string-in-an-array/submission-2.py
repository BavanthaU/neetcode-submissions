from collections import Counter
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        seen = Counter(arr)
        count = 0
        
        for key, val in seen.items():
            if val ==1:
                count+=1
                if count == k:
                    return key

        
        return ""
        