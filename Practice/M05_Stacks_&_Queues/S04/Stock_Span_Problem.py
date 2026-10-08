'''
stock span problem:
for every day prices -- no.of consecutive previous days which is lessthan or equal to curr day price 
'''
#brute force algorithm:
'''
find length of your days 
initialize span with [1] upto size  
traverse from left to right:
    check the previous 
    while j>=0 and price[j] <= price[i]
        increase span[i] += 1 
        decrease j 
store every day span 
return span
'''
def stock_span1(prices):
    n = len(prices)
    span = [1] * n 
    for i in range(n):
        j = i-1 
        while j>=0 and prices[j]<=prices[i]:
            span[i] += 1 
            j -= 1  
    return span 
prices = [100,80,60,70,60,75,85]
print(stock_span1(prices))


'''
optimal solution algorithm:
1.initialize empty stack 
2.initialize empty span 
3.traverse from left to right :
    while 
'''
def Stock_span2(prices):
    stack = []
    span = []
    for i in range(len(prices)):
        while stack and prices[stack[-1]] <= prices[i]:
            stack.pop()
        if not stack:
            span.append(i+1)
        else:
            span.append(i-stack[-1])
        stack.append(i)
    return span 
prices = [100,80,60,70,60,75,85]
print(Stock_span2(prices))