# nums = [1,2,3,4]
# res = []
# s = 0
# for i in range(len(nums)):
#     s += nums[i]
#     res.append(s)
# print(res)
# for i in range(1,len(nums)):
#     nums[i] = nums[i] + nums[i-1]
# print(nums)
'''1732'''
from typing import List
def largestAltitude(gain: List[int]) -> int:
        # n = len(gain)
        # arr = [0]*(n+1)
        # for i in range(1,n+1):
        #     arr[i] = arr[i-1]+gain[i-1]
        # return max(arr)

        for i in range(1,len(gain)):
            gain[i] = gain[i] + gain[i-1]
        return max(0,max(gain))