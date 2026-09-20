class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_len = 0 
        print(num_set)
        for i in num_set:
            if i-1 not in num_set:
                out = []
                out.append(i)
                j =i
                while j+1 in num_set:
                    out.append(i+1)
                    j+=1
                max_len = max(max_len, len(out) )
        
        return max_len
        