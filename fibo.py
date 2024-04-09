def fibonacci(n):
    fib = [0, 1]  
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2]) 
    return fib
n = int(input("Enter the number of Fibonacci numbers to generate: "))
fib_sequence = fibonacci(n)
print("Fibonacci sequence up to", n, "terms:")
print(fib_sequence)
