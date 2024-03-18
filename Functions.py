def generate_fibonacci_sequence(n):
    fibonacci_sequence = [0,1] #Initialize the sequence with the first two terms

    # Genetate Fibonacci sequence upto n terms 
    for i in range(2, n):
        next_term = fibonacci_sequence[_1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_term)

        return fibonacci_sequence
    
    def main():
        # Ask the user to input the value of n
        n = int(input("Enter the number of terms in the Fibonacci sequence: "))

        # Call the function to generate fibonacci sequence
        fibonacci_sequence = generate_fibonacci_sequence(n)

        # Print the generated Fibonacci sequence 
        print("Fibonacci sequence up to {}terms:".format(n))
        print(fibonacci_sequence)

        if __name__ == "__ main__":
            main()