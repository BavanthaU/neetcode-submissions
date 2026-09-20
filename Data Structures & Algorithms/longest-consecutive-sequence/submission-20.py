class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_len = 0 
        n = 0
        for i in num_set:
            if i-1 not in num_set:
                n+=1
                j =i
                while j+1 in num_set:
                    n+=1
                    j+=1
                max_len = max(max_len, n )
                n =0
        
        return max_len
        