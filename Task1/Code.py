n = int(input("Enter the number of terms in the Fibonacci series: "))
a = 0
b = 1
print("Fibonacci series:")
for i in range(n):
    print(a)  # Print the current term
    # Update the values for the next term
    next_term = a + b
    a = b
    b = next_term