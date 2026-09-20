class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_set = {}
        for i, num1 in enumerate(nums):
            num2 = target - num1
            if num2 in num_set:
                return [num_set[num2], i]
            else:
                num_set[num1] = i

        