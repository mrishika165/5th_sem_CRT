from typing import List
'''74'''
# def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    # arr = []
    # for row in matrix:
    #     arr += row 
    # left = 0 
    # right = len(arr)-1
    # while left<=right:
    #     mid = (left+right)//2
    #     if arr[mid] == target:
    #         return True 
    #     elif arr[mid]<target:
    #         left = mid + 1
    #     else:
    #         right = mid - 1
    # return False
#     

'''240'''
# def searchMatrix(matrix: List[List[int]], target: int) -> bool:
#     m = len(matrix)
#     n = len(matrix[0])
#     row,col = 0, n -1
#     while row<m and col>=0:
#         if target == matrix[row][col]:
#             return True 
#         elif target<matrix[row][col]:
#             col -= 1 
#         else:
#             row += 1 
#     return False
# matrix =[[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
# target = 5 
# print(searchMatrix(matrix,target))
