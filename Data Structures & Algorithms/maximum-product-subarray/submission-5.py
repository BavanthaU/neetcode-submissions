class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        max_dp= min_dp = nums[0]
        curr_max = curr_min = nums[0]

        for i in range(1, len(nums)):
            curr_max, curr_min  = max(nums[i], curr_max*nums[i], curr_min*nums[i]) , min(nums[i], curr_max*nums[i], curr_min*nums[i])
            max_dp = max(curr_max, max_dp)
            min_dp = min(curr_min, min_dp)
        return max_dp
