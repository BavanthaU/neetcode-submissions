# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         str1 = dict()
#         str2 = dict()
#         if len(s)!= len(t):
#             return False

#         for i in range(len(s)):
#             if s[i] in str1:
#                 str1[s[i]]+=1
#             else:
#                 str1[s[i]]=1

#         for i in range(len(t)):
#             if t[i] in str2:
#                 str2[t[i]]+=1
#             else:
#                 str2[t[i]]=1
        
#         for key, val in str1.items():
#             if key in str2:
#                 if str2[key]!= val:
#                     return False
#             else:
#                 return False
        
#         return True
            
from collections import Counter 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        s_count = Counter(s)
        t_count = Counter(t)
        return s_count == t_count


