# class Solution:
#     def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
#         out = []

#         for i , t in enumerate(temperatures):
#             n=i
#             while i < len(temperatures)-1 and t >= temperatures[i+1]:
#                 i+=1
#             if i < len(temperatures)-1 and t < temperatures[i+1]:
#                 out.append(i-n +1)
#             else:
#                 out.append(0)        
#         return out


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):

            while stack and temp > temperatures[stack[-1]]:
                prev_i = stack.pop()
                result[prev_i] = i - prev_i

            stack.append(i)

        return result