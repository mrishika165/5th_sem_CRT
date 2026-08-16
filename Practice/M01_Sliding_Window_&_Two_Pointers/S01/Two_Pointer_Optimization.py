'''
input: [12,45,63,20,96,25,10]
output:[12,20,96,10]
'''
# n = list(map(int,input().split()))
# res = []
# for i in n:
#     if i % 2 == 0:
#         res.append(i)
# print(res)
# arr = list(map(int,input().split()))
# for ele in arr:
#     if ele % 2 != 0:
#         arr.remove(ele)
# print(arr)

# arr = list(map(int,input().split()))
# i = 0
# for j in range(len(arr)):
#     if arr[j] % 2 == 0:
#         arr[i] = arr[j]
#         i += 1
        
# print(arr[:i])

s = input()
li = list(s)
left = 0
right = len(s)-1
while left<right:
    li[left],li[right] = li[right],li[left]
    left +=1
    right -=1
print("".join(li))