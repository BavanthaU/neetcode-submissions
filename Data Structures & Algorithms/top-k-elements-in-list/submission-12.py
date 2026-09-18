class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        vals = dict()
        out =[]

        for i in nums:
            if i in vals:
                vals[i]+=1
            else:
                vals[i]=1
        
        vals_sorted = dict(sorted(vals.items(), key=lambda x:x[1], reverse=True))
        for i, key in enumerate(vals_sorted):
            if i < k:
                out.append(key)
        
        return out