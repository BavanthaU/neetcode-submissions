# from collections import defaultdict 
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         ang_list = defaultdict(list)

#         for str1 in strs:
#             srt_str1 = ''.join(sorted(str1))
#             ang_list[srt_str1].append(str1)
#         return list(ang_list.values())

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord('a')] += 1

            groups[tuple(count)].append(s)

        return list(groups.values())