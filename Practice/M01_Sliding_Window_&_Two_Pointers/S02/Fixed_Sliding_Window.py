'''
643
1343
1456
2269
2379
'''
# from typing import List
# def findMaxAverage(nums: List[int], k: int) -> float:
#         n = len(nums)
#         max_sum= float("-inf") 
#         for i in range(0,n-k+1):
#             sub_sum = 0 
#             for j in range(i,k+i):
#                 sub_sum += nums[j]
#             max_sum = max(sub_sum,max_sum)
#         return max_sum/k
# nums = [1,12,-5,-6,50,3]
# k = 4
# print(findMaxAverage(nums,k))
# from typing import List
# def findMaxAverage(self, nums: List[int], k: int) -> float:
#     window = nums[0:k]
#     window_sum = sum(window)
#     max_sum = window_sum
#     n = len(nums)
#     for i in range(0,n-k):
#         window_sum = window_sum - nums[i]+nums[k+i]
#         max_sum = max(max_sum,window_sum)
#     return max_sum/k
# nums = [1,12,-5,-6,50,3]
# k = 4
# print(findMaxAverage(nums,k))


'''
1343
'''
from typing import List
def numOfSubarrays(arr: List[int], k: int, threshold: int) -> int:
    win_sum = sum(arr[0:k])
    count = 0 
    if (win_sum/k)>=threshold:
        count += 1
    n = len(arr)
    for i in range(n-k):
        win_sum = win_sum - arr[i] + arr[k+i]
        if (win_sum/k) >= threshold:
            count+=1
    return count
arr = [2,2,2,2,5,5,5,8]
threshold = 4 
k = 3 
print(numOfSubarrays(arr,k,threshold))

