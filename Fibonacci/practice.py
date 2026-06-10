#fibonacci

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
nums = 10
for i in range(nums):
    print(fibonacci(i), end=" ")