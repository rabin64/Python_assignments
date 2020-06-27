# 19. Write a Python program to create Fibonacci series upto n using Lambda.

fibonacci = lambda num: 0 if num == 0 else (1 if num == 1 else fibonacci(num - 1) + fibonacci(num - 2) )
print(fibonacci(10))
