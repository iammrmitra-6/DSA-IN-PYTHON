# Program to generate the n-th Fibonacci term using a loop without a function

# 1. Get input from the user for the term number (n)
n = int(input("Enter the term number (n): "))

# 2. Initialize the first two Fibonacci terms
# F0 = 0, F1 = 1 (using 1-based indexing: 1st term is 0, 2nd term is 1)
first_term = 0
second_term = 1
result = 0

# 3. Handle edge cases for n <= 2
if n <= 0:
    print("Invalid input. Please enter a positive integer for the term number.")
elif n == 1:
    # The 1st term is 0
    result = first_term
elif n == 2:
    # The 2nd term is 1
    result = second_term
else:
    # 4. Use a loop to calculate the n-th term for n > 2
    # The loop iterates (n-2) times to find the terms from the 3rd to the n-th
    for i in range(2, n):
        # Calculate the next term
        next_term = first_term + second_term
        
        # Update first_term and second_term for the next iteration
        first_term = second_term
        second_term = next_term
        
        # The 'second_term' variable will hold the final result after the loop finishes
        result = second_term

# 5. Print the final result
if n > 0:
    print(f"The {n}-th term of the Fibonacci series is: {result}")
