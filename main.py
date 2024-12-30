def main():
    # Step 1: Define required variables
    n = int(input("Enter the number of Fibonacci numbers you want: "))  # User input for the number of Fibonacci numbers
    
    # Initialize the first two Fibonacci numbers
    a, b = 0, 1

    # Step 2: Start the loop to generate Fibonacci numbers
    print("Fibonacci sequence:")
    for _ in range(n):  # Loop to generate 'n' Fibonacci numbers
        print(a)         # Print the current Fibonacci number
        a, b = b, a + b  # Update 'a' and 'b' to the next two Fibonacci numbers

# Run the main function
main()
