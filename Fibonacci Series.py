n = int(input("Enter the value of n: "))  # Take user input

print("\nRecursive Approach")

def fibonacci_recursive(n, a=0, b=1):
    if a > n:  # Base case: Stop recursion when `a` exceeds `n`
        return
    print(a, end=" ")  # Print current Fibonacci number
    fibonacci_recursive(n, b, a + b)  # Recursive call with updated values

fibonacci_recursive(n)  # Call the function

print("\nIterative Approach")

def fibonacci(n):
    a, b = 0, 1
    while a <= n:
        print( a, end=" ")
        a, b = b, a+b

fibonacci(n)