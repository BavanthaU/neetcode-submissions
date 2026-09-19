# class Solution:
#     def isValidSudoku(self, board: List[List[str]]) -> bool:
#         row = set()

#         for i in range(len(board)):
#             row.clear()
#             for j in board[i]:
#                 if j not in row and j !='.':
#                     row.add(j)
#                 else:
#                     if j!='.':
#                         return False

#         for i in range(len(board)):
#             row.clear()
#             col = [board[t][i] for t in range(9)]
#             for j in col:
#                 if j not in row and j!='.':
#                     row.add(j)
#                 else:
#                     if j!='.':
#                         return False
        
#         for i in range(3):
#             mat3x9 = board[3*i:3*i+3]
#             for j in range(3):
#                 row.clear()
#                 mat3x3 = [row_3[3*j:3*j +3] for row_3 in mat3x9]
#                 for r in range(3):
#                     for c in range(3):
#                         val = mat3x3[r][c]
#                         if val not in row and val !='.':
#                             row.add(val)
#                         else:
#                             if val!='.':
#                                 return False

#         return True

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                val = board[r][c]

                if val == '.':
                    continue

                box = (r // 3) * 3 + (c // 3)

                if val in rows[r] or val in cols[c] or val in boxes[box]:
                    return False

                rows[r].add(val)
                cols[c].add(val)
                boxes[box].add(val)

        return True
                