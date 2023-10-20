def fibonacci_non_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    fib_sequence = [0, 1]
    
    for i in range(2, n + 1):
        next_fib = fib_sequence[i - 1] + fib_sequence[i - 2]
        fib_sequence.append(next_fib)
    
    return fib_sequence[n]

def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

n=10
print(fibonacci_non_recursive(n))
print(fibonacci_recursive(n))