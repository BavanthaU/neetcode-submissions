from collections import defaultdict 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ang_list = defaultdict(list)

        for str1 in strs:
            srt_str1 = ''.join(sorted(str1))
            ang_list[srt_str1].append(str1)
        return list(ang_list.values())
