'''
Monotonic of stacks:
arranging of elements in a particular either in increasing or decreasing 
2 ways 
1.Monotonic of increasing order
2.Monotic of decreasing order
'''

'''
Algorithm:
1.Initialize empty stack 
2.Iterate every element
3.for every element:
     --> stack should not be empty and top element should be greater than curr element
         -->remove the element 
4.insert the curr element 
5.in the output it will be monotonic of increasing order elements
'''

# def monotonic_increase(arr):
#     stack = []
#     for num in arr:
#         while stack and stack[-1]>num:
#             stack.pop()
#         stack.append(num)
#     return stack
# arr = [1, 3, 2, 4, 5]
# print(monotonic_increase(arr))

# def monotonic_decrease(arr):
#     stack = []
#     for num in arr:
#         while stack and stack[-1]<num:
#             stack.pop()
#         stack.append(num)
#     return stack
# arr = [1, 3, 2, 4, 5]
# print(monotonic_decrease(arr))


#1.To find next greater2 element 
'''
find len of arr
create a result array with -1 values
create empty stack 
traverse the array from left to right 
for every index:
    while stack is not empty and arr[stack[-1]]<arr[i]:
        pop the top index 
        store arr[i] as next greater ele 
after traversal, all indexes remaining in the stack , returns -1 
return res array
'''
# def next_greater(arr):
#     n = len(arr)
#     res = [-1] * n 
#     for i in range(n):
#         for j in range(i+1,n):
#             if arr[j]>arr[i]:
#                 res[i] = max(res[i],arr[j])
#     return res 
# arr = [20,30,45,7,8]
# print(next_greater(arr))


# def next_greater2(arr):
#     n = len(arr)
#     res = [-1] * n 
#     stack = []
#     for i in range(n):
#         while stack and arr[stack[-1]]<arr[i]:
#             index = stack.pop()
#             res[index] = arr[i]
#         stack.append(i)
#     return res 
# arr = [2,1,2,5,8]
# print(next_greater2(arr))


#to find prev greater element 
def prev_greater(arr):
    n = len(arr)
    res = [-1] * n 
    stack = []
    for i in range(n):
        while stack and arr[stack[-1]]>arr[i]:
            index = stack.pop()
            res[index] = arr[i]
        stack.append(i)
    return res 
arr = [2,1,2,5,8]
print(prev_greater(arr))



