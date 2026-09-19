class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        max_length = 1
        if nums:
            s_nums = sorted(nums)
            print(s_nums)
            cont_seq = set()

            left = 0 
            while left< len(nums)-1:
                cont_seq.add(s_nums[left])
                if s_nums[left+1] not in cont_seq:
                    if s_nums[left+1] == s_nums[left]+1:
                        cont_seq.add(s_nums[left+1])
                        max_length = max(max_length, len(cont_seq))
                        left+=1
                    else:
                        cont_seq.clear()
                        left+=1
                else:
                    left+=1
        else:
            max_length = 0
                
        
        return max_length