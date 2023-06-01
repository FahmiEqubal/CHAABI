# Calculate the factorial of a number using lambda function

factorial = lambda n: 1 if n == 0 else n * factorial(n - 1)

number = 5
result = factorial(number)

print(f"The factorial of {number} is {result}")
