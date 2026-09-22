# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         if len(nums) == 1:
#             return nums[0]

#         dp = [0] * len(nums)

#         dp[0] = nums[0]
#         dp[1] = max(nums[0], nums[1])

#         for i in range(2, len(nums)):
#             dp[i] = max(dp[i-1], (nums[i]+dp[i-2]))

#         return dp[-1]


#recursion
class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def solve(i):
            if i < 0:
                return 0

            if i in memo:
                return memo[i]

            memo[i] = max(
                solve(i - 1),
                nums[i] + solve(i - 2)
            )

            return memo[i]

        return solve(len(nums) - 1)