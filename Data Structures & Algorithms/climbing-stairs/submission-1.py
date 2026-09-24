class Solution:
    def climbStairs(self, n: int) -> int:
        if n<= 2:
            return n 
        
        one_step_earlier = 2
        two_steps_earlier = 1

        for _ in range(3,n+1):
            current = one_step_earlier + two_steps_earlier
            two_steps_earlier = one_step_earlier
            one_step_earlier = current
        
        return one_step_earlier
        