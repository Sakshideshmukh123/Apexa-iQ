import sys
import os

# Redirect all print output to output.txt in the same folder
output_file = os.path.join(os.path.dirname(__file__), 'output.txt')
sys.stdout = open(output_file, 'w')

# ----------------- Pattern functions -----------------
def print_pyramid(height):
    """Print a pyramid pattern of asterisks."""
    for i in range(1, height + 1):
        spaces = " " * (height - i)
        stars = "*" * (2 * i - 1)
        print(spaces + stars)

def print_diamond(height):
    """Print a diamond pattern of asterisks."""
    # Upper half of diamond
    for i in range(1, height + 1):
        spaces = " " * (height - i)
        stars = "*" * (2 * i - 1)
        print(spaces + stars)
    
    # Lower half of diamond
    for i in range(height - 1, 0, -1):
        spaces = " " * (height - i)
        stars = "*" * (2 * i - 1)
        print(spaces + stars)

def print_number_pattern(rows):
    """Print a number pattern."""
    for i in range(1, rows + 1):
        line = ""
        for j in range(1, i + 1):
            line += str(j) + " "
        print(line)

# ----------------- Example usage -----------------
if __name__ == "__main__":
    print("Pyramid Pattern (height 5):")
    print_pyramid(5)
    
    print("\nDiamond Pattern (height 5):")
    print_diamond(5)
    
    print("\nNumber Pattern (5 rows):")
    print_number_pattern(5)

# Close the redirected stdout
sys.stdout.close()
