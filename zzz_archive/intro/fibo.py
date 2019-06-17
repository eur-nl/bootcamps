# Fibonacci numbers module

test_variable = 100

# write Fibonacci series up to n
def fib(n):
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
    print()
