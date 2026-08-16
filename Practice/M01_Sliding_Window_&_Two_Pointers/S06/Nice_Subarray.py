'''1248'''
from typing import List
# def numberOfSubarrays(nums: List[int], k: int) -> int:
#     def sub_arr(k):
#         left,count,odds = 0,0,0
#         if k<0:
#             return 0
#         for right in range(len(nums)):
#             if nums[right]%2 == 1:
#                 odds += 1 
#             while odds>k:
#                 if nums[left]%2 == 1:
#                     odds-=1 
#                 left += 1 
#             count += right-left+1 
#         return count 
#     return sub_arr(k) - sub_arr(k-1)
# nums = [1,1,2,1,1]
# k = 3 
# print(numberOfSubarrays(nums,k))
'''1763'''

def longestNiceSubstring(self,s: str) -> str:
    if len(s) < 2:
        return ""
    unique = set(s)
    for i,ch in enumerate(s):
        if ch.lower() in unique and ch.upper() in unique:
            continue
        left_str = self.longestNiceSubstring(s[:i])
        right_str = self.longestNiceSubstring(s[i+1:])
        return left_str if len(left_str) >= len(right_str) else right_str
    return s
s = "YazaAay"
print(longestNiceSubstring(s))