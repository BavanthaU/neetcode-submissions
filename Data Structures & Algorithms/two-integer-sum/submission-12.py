class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_set = set()

        for i, num1 in enumerate(nums):
            num2 = target - num1
            if num2 in num_set:
                return [nums.index(num2), i]
            else:
                num_set.add(num1)

        