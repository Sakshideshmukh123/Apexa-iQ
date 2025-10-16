import sys
import os

# Redirect all print output to output.txt in the same folder
output_file = os.path.join(os.path.dirname(__file__), 'output.txt')
sys.stdout = open(output_file, 'w')

# ----------------- Fibonacci functions -----------------
def fibonacci_iterative(n):
    """Generate Fibonacci sequence up to n terms using iteration."""
    fib_sequence = [0, 1]
    
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return fib_sequence
    
    for i in range(2, n):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
    
    return fib_sequence

def fibonacci_recursive(n):
    """Calculate the nth Fibonacci number using recursion."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# ----------------- Example usage -----------------
if __name__ == "__main__":
    n_terms = 10

    # Iterative approach
    print(f"Fibonacci sequence (first {n_terms} terms):")
    print(fibonacci_iterative(n_terms))
    
    # Recursive approach (for individual terms)
    print("\nFibonacci sequence using recursion:")
    for i in range(n_terms):
        print(f"F({i}) = {fibonacci_recursive(i)}")

# Close the redirected stdout
sys.stdout.close()
