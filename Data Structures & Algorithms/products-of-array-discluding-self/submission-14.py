import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums.count(0) == 0:
            max_sum = math.prod(nums)
            out = []
            if max_sum !=0:
                for i, num in enumerate(nums):
                    out.append(max_sum//num)
                return out
        elif nums.count(0) == 1:
            out = [0] *len(nums)
            idx = nums.index(0)
            nums.remove(0)
            out[idx] = math.prod(nums)
            return out
        else:
            return [0] *len(nums)
            



        