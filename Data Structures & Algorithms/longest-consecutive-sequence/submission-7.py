class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        num_set = set(nums)
        max_length = 0

        for num in num_set:
            # Only start counting if num is the beginning
            if num - 1 not in num_set:
                current = num
                current_length = 1

                while current + 1 in num_set:
                    current += 1
                    current_length += 1

                max_length = max(max_length, current_length)

        return max_length

# class Solution:
#     def longestConsecutive(self, nums: list[int]) -> int:
#         num_set = set(nums)
#         max_length = 1
#         if nums:
#             for i in range(len(nums)):
#                 num = nums[i]
#                 if num-1 not in num_set:
#                     tmp =[]
#                     tmp.append(nums)
#                     while True:
#                         if num+1 in num_set:
#                             tmp.append(num+1)
#                             max_length = max(len(tmp), max_length)
#                             num+=1
#                         else:
#                             break
#         else:
#             max_length = 0
#         return max_length
# class Solution:
#     def longestConsecutive(self, nums: list[int]) -> int:
#         max_length = 1
#         if nums:
#             s_nums = sorted(nums)
#             print(s_nums)
#             cont_seq = set()

#             left = 0 
#             while left< len(nums)-1:
#                 cont_seq.add(s_nums[left])
#                 if s_nums[left+1] not in cont_seq:
#                     if s_nums[left+1] == s_nums[left]+1:
#                         cont_seq.add(s_nums[left+1])
#                         max_length = max(max_length, len(cont_seq))
#                         left+=1
#                     else:
#                         cont_seq.clear()
#                         left+=1
#                 else:
#                     left+=1
#         else:
#             max_length = 0
                
        
#         return max_length