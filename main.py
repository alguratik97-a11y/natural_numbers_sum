# Program to find the sum of natural numbers up to 'n'

# Taking input from the user
n = int(input("Enter a positive integer: "))

# Initializing sum variable
sum_result = 0

# Using a for loop to calculate the sum
for i in range(1, n + 1):
    sum_result += i

# Displaying the final result
print(f"The sum of natural numbers up to {n} is: {sum_result}")
