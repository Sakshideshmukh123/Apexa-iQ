import sys
import os

# Redirect all print output to output.txt in the same folder with line buffering
output_file = os.path.join(os.path.dirname(__file__), 'output.txt')
sys.stdout = open(output_file, 'w', buffering=1)  # line buffering for faster write

# ----------------- Palindrome functions -----------------
def is_palindrome_string(s):
    """Check if a string is a palindrome."""
    s = ''.join(e.lower() for e in s if e.isalnum())
    return s == s[::-1]

def is_palindrome_number(n):
    """Check if a number is a palindrome."""
    return str(n) == str(n)[::-1]

def find_palindromes_in_list(items):
    """Find all palindromes in a list of strings or numbers."""
    palindromes = []
    
    for item in items:
        if isinstance(item, str):
            if is_palindrome_string(item):
                palindromes.append(item)
        elif isinstance(item, (int, float)):
            if is_palindrome_number(item):
                palindromes.append(item)
    
    return palindromes

# ----------------- Example usage -----------------
if __name__ == "__main__":
    # String palindromes
    test_strings = ["racecar", "hello", "A man, a plan, a canal, Panama", "python", "Madam"]
    
    print("String palindrome check:")
    for s in test_strings:
        print(f"'{s}' is a palindrome: {is_palindrome_string(s)}")
    
    # Number palindromes
    test_numbers = [121, 12321, 12345, 1001, 7, 678]
    
    print("\nNumber palindrome check:")
    for n in test_numbers:
        print(f"{n} is a palindrome: {is_palindrome_number(n)}")
    
    # Find palindromes in a mixed list
    mixed_list = ["racecar", 121, "python", 12321, "hello", 678]
    palindromes = find_palindromes_in_list(mixed_list)
    
    print("\nPalindromes in the mixed list:")
    print(palindromes)

# Close the redirected stdout
sys.stdout.close()
