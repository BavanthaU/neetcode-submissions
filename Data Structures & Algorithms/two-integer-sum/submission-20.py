class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numHash = {}
        for i, num1 in enumerate(nums):
            num2 = target - num1
            if num2 in numHash:
                return [numHash[num2], i]
            else:
                numHash[num1] = i

        