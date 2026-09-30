# class Solution:
#     def minCostClimbingStairs(self, cost: List[int]) -> int:
#         dp = [0] * (len(cost) +1)

#         dp[0] = dp[1]= 0        
        
#         for i in range(2, len(cost)+1):
#             dp[i] = min(dp[i-1]+cost[i-1] , dp[i-2]+cost[i-2])
        
#         return dp[-1]

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        one_step = 0
        two_step = 0

        for i in range(2, len(cost)+1):
            curr = min(one_step+cost[i-1] , two_step+cost[i-2])
            two_step = one_step
            one_step = curr
        
        return one_step