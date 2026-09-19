import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = [0]*len(nums)
        if 0 not in nums:
            max_mul = math.prod(nums)
            for i in range(len(nums)):
                out[i] = max_mul//nums[i]
        else:
            if nums.count(0) == 1:
                idx = nums.index(0)
                nums[idx] = 1
                out[idx] = math.prod(nums)
            else:
                return out

        return out

        