class Solution:
    # def twoSum(self, nums: list[int], target: int) -> list[int]:
    #     num_dict = dict()
    #     for i, val in enumerate(nums):
    #         if val in num_dict:
    #             tmp_val = [num_dict[val]]
    #             tmp_val.append(i)
    #             num_dict[val] = tmp_val
    #         else:
    #             num_dict[val] = i
    #     print(num_dict)
    #     for num1 in num_dict:
    #         num2 = target - num1
    #         if num2 in num_dict:
    #             if num1 == num2:
    #                 if type(num_dict[num1]) is list:
    #                     return num_dict[num1]
    #             else:
    #                 return [num_dict[num1] , num_dict[num2]]

    def twoSum(self, nums : list[int], target: int)->list[int]:
        seen = dict()
        for i, val in enumerate(nums):
            other_number = target-val
            if other_number in seen:
                return [seen[other_number], i]
            seen[val] = i

        return [0,0]