class Solution:
    def isValid(self, s: str) -> bool:
        par_dic = {')':'(', ']':'[', '}':'{'}
        par_list =[]
        for i in s:
            if i in par_dic:
                if par_list:
                    if par_dic[i] != par_list.pop():
                        return False
                else:
                    return False

            else:
                par_list.append(i)
        
        return not par_list





        