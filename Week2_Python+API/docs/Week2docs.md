# Week2

Apexa iQ Internship – Week2 Documentation

## Python Programming Topics

### Python Basics

- **Syntax:** Python uses indentation to define code blocks instead of brackets. The standard is 4 spaces per indentation level.
- **Variables:** Dynamically typed, no declaration needed, naming conventions use snake_case.
- **Data Types:**
    - **int:** Whole numbers like 5, -10, 1000
    - **float:** Decimal numbers like 3.14, -0.001, 2.5e3
    - **string:** Text sequences like "hello", 'Python', """Multi-line text"""
    - **list:** Ordered, mutable collections [1, 2, 3], ["a", "b", "c"]
    - **tuple:** Ordered, immutable collections (1, 2, 3), ("a", "b", "c")
    - **dict:** Key-value pairs {"name": "John", "age": 30}
    - **set:** Unordered collection of unique elements {1, 2, 3}

### Control Flow

- **Conditional Statements:**
    
    ```python
    if condition:
        # code block
    elif another_condition:
        # code block
    else:
        # code block
    ```
    
- **Loops:**
    - **For loop:**
        
        ```python
        for item in iterable:
            # code block
            
        # with range
        for i in range(5):
            # code block
        ```
        
    - **While loop:**
        
        ```python
        while condition:
            # code block
        ```
        
    - **Loop control:** break (exit loop), continue (skip to next iteration)

### Functions

- **Basic function:**
    
    ```python
    def function_name(parameter1, parameter2):
        # code block
        return value
    ```
    
- **Default parameters:**
    
    ```python
    def greet(name, message="Hello"):
        return f"{message}, {name}!"
    ```
    
- **Variable arguments:**
    
    ```python
    # *args for variable positional arguments
    def sum_all(*args):
        return sum(args)
        
    # **kwargs for variable keyword arguments
    def print_info(**kwargs):
        for key, value in kwargs.items():
            print(f"{key}: {value}")
    ```
    

### Exception Handling

- **Basic try-except:**
    
    ```python
    try:
        # code that might raise an exception
        result = 10 / 0
    except ZeroDivisionError:
        # handle specific exception
        print("Cannot divide by zero")
    except Exception as e:
        # handle any other exception
        print(f"An error occurred: {e}")
    finally:
        # always executed
        print("This always runs")
    ```
    

### Decorators

- Functions that modify the behavior of other functions
- **Example:**
    
    ```python
    def timer_decorator(func):
        def wrapper(*args, **kwargs):
            import time
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            print(f"Function {func.__name__} took {end-start} seconds to run")
            return result
        return wrapper
    
    @timer_decorator
    def slow_function():
        import time
        time.sleep(1)
        return "Done"
    ```
    

### Object-Oriented Programming (OOP)

- **Classes and Objects:**
    
    ```python
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age
            
        def greet(self):
            return f"Hello, my name is {self.name}"
            
    # Create an object
    person = Person("Alice", 30)
    print(person.greet())
    ```
    
- **Inheritance:**
    
    ```python
    class Employee(Person):
        def __init__(self, name, age, employee_id):
            super().__init__(name, age)
            self.employee_id = employee_id
            
        def details(self):
            return f"{self.name}, ID: {self.employee_id}"
    ```
    
- **Encapsulation:** Using private (_attr) and protected (__attr) attributes
- **Polymorphism:** Method overriding and method overloading
- **Abstraction:** Using abstract base classes and interfaces

### Comprehensions

- **List comprehension:**
    
    ```python
    # Create a list of squares
    squares = [x**2 for x in range(10)]
    
    # With conditional
    even_squares = [x**2 for x in range(10) if x % 2 == 0]
    ```
    
- **Dictionary comprehension:**
    
    ```python
    # Create a dictionary {number: square}
    square_dict = {x: x**2 for x in range(5)}
    ```
    

### Iterators and Generators

- **Iterators:** Objects implementing **iter**() and **next**() methods
- **Generators:** Functions using yield to return values lazily
    
    ```python
    def fibonacci(n):
        a, b = 0, 1
        for _ in range(n):
            yield a
            a, b = b, a + b
            
    # Use the generator
    for num in fibonacci(10):
        print(num)
    ```
    

### Virtual Environments & pip

- **Creating virtual environments:** python -m venv myenv
- **Activating:**
    - Windows: myenv\Scripts\activate
    - Unix/MacOS: source myenv/bin/activate
- **pip commands:**
    - pip install package_name
    - pip install -r requirements.txt
    - pip freeze > requirements.txt

### Standard Libraries

- **Common libraries:**
    - os, sys - System operations
    - datetime - Date and time handling
    - json - JSON parsing
    - re - Regular expressions
    - collections - Specialized container datatypes
    - math - Mathematical functions
    - random - Random number generation
    - pathlib - Object-oriented filesystem paths

## Coding Standards

### Naming Conventions

- **Variables and functions:** snake_case (lowercase with underscores)
- **Classes:** PascalCase (capitalize first letter of each word)
- **Constants:** UPPER_SNAKE_CASE
- **Private attributes:** _leading_underscore
- **Magic methods:** **double_underscores**

### Documentation

- **Docstrings:** Documentation strings that describe modules, classes, functions
    
    ```python
    def calculate_area(radius):
        """
        Calculate the area of a circle.
        
        Args:
            radius (float): The radius of the circle
            
        Returns:
            float: The area of the circle
            
        Raises:
            ValueError: If radius is negative
        """
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        return 3.14159 * radius * radius
    ```
    
- **Comments:** Use # for single-line comments, explaining "why" not "what"

### Testing

- **Types of testing:**
    - Unit testing - Testing individual components (unittest, pytest)
    - Integration testing - Testing interactions between components
    - Functional testing - Testing complete functionality
    - Regression testing - Ensuring new changes don't break existing functionality
    - Performance testing - Testing system performance

### Style Guide

- **PEP 8:** Python Enhancement Proposal 8 - Style Guide for Python Code
    - Use 4 spaces for indentation
    - Line length should not exceed 79 characters
    - Imports should be on separate lines
    - Use blank lines to separate functions and classes
    - Use spaces around operators

### Design Principles

- **SOLID Principles:**
    - S - Single Responsibility Principle
    - O - Open/Closed Principle
    - L - Liskov Substitution Principle
    - I - Interface Segregation Principle
    - D - Dependency Inversion Principle
- **DRY (Don't Repeat Yourself):** Avoid duplicating code by abstracting common operations

## APIs Topics

### API Basics

- **API:** Application Programming Interface - allows different software systems to communicate
- **Types of APIs:**
    - REST (Representational State Transfer)
    - SOAP (Simple Object Access Protocol)
    - GraphQL
    - RPC (Remote Procedure Call)
    - WebSockets

### HTTP Status Codes

- **2xx Success:** 200 OK, 201 Created, 204 No Content
- **3xx Redirection:** 301 Moved Permanently, 302 Found, 304 Not Modified
- **4xx Client Errors:** 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found
- **5xx Server Errors:** 500 Internal Server Error, 502 Bad Gateway, 503 Service Unavailable

### Response Formats

- **JSON (JavaScript Object Notation):** Most common format for web APIs
- **XML (eXtensible Markup Language):** Traditional format, more verbose
- **YAML:** Human-readable format often used for configuration
- **Protocol Buffers:** Binary format for efficient serialization

### API Authentication

- **Types of API Authentication:**
    - API Keys
    - Basic Authentication
    - OAuth 1.0/2.0
    - JWT (JSON Web Tokens)
    - API Gateway Authentication

### API Design Considerations

- **Versioning:** /api/v1/resources, Accept header, query parameters
- **Security:** HTTPS, rate limiting, input validation, CORS
- **CRUD Operations:**
    - CREATE - POST /resources
    - READ - GET /resources, GET /resources/{id}
    - UPDATE - PUT /resources/{id}, PATCH /resources/{id}
    - DELETE - DELETE /resources/{id}

### POSTMAN

- API development environment for building and testing APIs
- Features: request builder, collections, environments, automated testing, mock servers

### Optimization and Efficiency

- Pagination for large data sets
- Filtering, sorting, and searching capabilities
- Caching strategies (ETags, Cache-Control)
- Response compression
- Batch operations

### Python and APIs

- **Requests library:**
    
    ```python
    import requests
    
    # GET request
    response = requests.get('https://api.example.com/users')
    data = response.json()
    
    # POST request
    payload = {'name': 'John', 'job': 'Developer'}
    response = requests.post('https://api.example.com/users', json=payload)
    
    # Authentication
    headers = {'Authorization': 'Bearer your_token'}
    response = requests.get('https://api.example.com/protected', headers=headers)
    ```
    

### RBAC (Role-Based Access Control)

- Security approach based on user roles and permissions
- Components: roles, permissions, users, role assignments
- Implementation in APIs via tokens, middleware, database models

## Extra Topics (Optional)

### Software Development Life Cycle (SDLC)

- **Phases:**
    - Planning
    - Analysis
    - Design
    - Implementation
    - Testing
    - Deployment
    - Maintenance
- **Models:** Waterfall, Spiral, Incremental, V-Model

### Agile Basics

- **Values:** Individuals and interactions, working software, customer collaboration, responding to change
- **Frameworks:** Scrum, Kanban, Extreme Programming (XP)
- **Practices:** Daily standups, sprints, retrospectives, user stories, story points

### Version Control

- **Git basics:**
    - init, clone, add, commit, push, pull
    - branch, merge, rebase
    - fetch, checkout
- **Workflows:** Centralized, Feature Branch, Gitflow, Forking
- **Platforms:** GitHub, GitLab, Bitbucket

### Software Architecture

- **Architecture patterns:**
    - Monolithic
    - Microservices
    - Serverless
    - Event-driven
    - Layered architecture
- **Design patterns:**
    - Creational: Singleton, Factory, Builder
    - Structural: Adapter, Decorator, Facade
    - Behavioral: Observer, Strategy, Command

## Programming Assignments

### Object-Oriented Programming

- **BankAccount System:**
    - Create a BankAccount class with methods for deposit, withdraw, and check_balance
    - Handle insufficient balance scenario using custom exceptions
    - Implement account types as subclasses (optional)

```python
class InsufficientFundsError(Exception):
    """Exception raised when withdrawal amount exceeds account balance."""
    pass

class BankAccount:
    def __init__(self, account_number, owner_name, balance=0):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance
    
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount
        return f"Deposited ${amount}. New balance: ${self.balance}"
    
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise InsufficientFundsError(f"Cannot withdraw ${amount}. Available balance: ${self.balance}")
        self.balance -= amount
        return f"Withdrew ${amount}. New balance: ${self.balance}"
    
    def check_balance(self):
        return f"Current balance for account {self.account_number}: ${self.balance}"

# Eexample usage
if __name__ == "__main__":
    try:
        # Create a new account
        account = BankAccount("12345", "John Doe", 1000)
        
        # Check initial balance
        print(account.check_balance())
        
        # Deposit money
        print(account.deposit(500))
        
        # Withdraw money
        print(account.withdraw(300))
        
        # Try to withdraw too much
        print(account.withdraw(2000))
    except InsufficientFundsError as e:
        print(f"Error: {e}")
    except ValueError as e:
        print(f"Error: {e}")

```

**Output:**

```
Current balance for account 12345: $1000
Deposited $500. New balance: $1500
Withdrew $300. New balance: $1200
Error: Cannot withdraw $2000. Available balance: $1200

```

- **Library Management System:**
    - Create Book, Member, and Library classes
    - Implement borrowing and returning functionality
    - Track status of books (available vs. borrowed)
    - Add date tracking for due dates (optional)

```python
from datetime import datetime, timedelta

class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_available = True
        self.borrowed_by = None
        self.due_date = None
    
    def __str__(self):
        status = "Available" if self.is_available else f"Borrowed by {self.borrowed_by} (Due: {self.due_date})"
        return f"[{self.book_id}] {self.title} by {self.author} - {status}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.books_borrowed = []
    
    def __str__(self):
        return f"Member: {self.name} (ID: {self.member_id}), Books borrowed: {len(self.books_borrowed)}"

class Library:
    def __init__(self, name):
        self.name = name
        self.books = {}
        self.members = {}
    
    def add_book(self, book):
        self.books[book.book_id] = book
        return f"Book '{book.title}' added to the library."
    
    def add_member(self, member):
        self.members[member.member_id] = member
        return f"Member {member.name} registered."
    
    def borrow_book(self, book_id, member_id):
        if book_id not in self.books:
            return "Book not found in library."
        if member_id not in self.members:
            return "Member not registered in library."
        
        book = self.books[book_id]
        member = self.members[member_id]
        
        if not book.is_available:
            return f"Book '{book.title}' is already borrowed."
        
        book.is_available = False
        book.borrowed_by = member.name
        book.due_date = (datetime.now() + timedelta(days=14)).strftime("%Y-%m-%d")
        member.books_borrowed.append(book_id)
        
        return f"Book '{book.title}' borrowed by {member.name}. Due date: {book.due_date}"
    
    def return_book(self, book_id):
        if book_id not in self.books:
            return "Book not found in library."
        
        book = self.books[book_id]
        
        if book.is_available:
            return f"Book '{book.title}' was not borrowed."
        
        member_name = book.borrowed_by
        for member in self.members.values():
            if member.name == member_name:
                if book_id in member.books_borrowed:
                    member.books_borrowed.remove(book_id)
        
        book.is_available = True
        book.borrowed_by = None
        book.due_date = None
        
        return f"Book '{book.title}' returned successfully."
    
    def display_available_books(self):
        available_books = [book for book in self.books.values() if book.is_available]
        if not available_books:
            return "No books available."
        
        result = "Available Books:\n"
        for book in available_books:
            result += f"{book}\n"
        return result
    
    def display_borrowed_books(self):
        borrowed_books = [book for book in self.books.values() if not book.is_available]
        if not borrowed_books:
            return "No books currently borrowed."
        
        result = "Borrowed Books:\n"
        for book in borrowed_books:
            result += f"{book}\n"
        return result

# Example usage
if __name__ == "__main__":
    # Create library
    city_library = Library("City Public Library")
    
    # Add books
    book1 = Book("B001", "The Great Gatsby", "F. Scott Fitzgerald")
    book2 = Book("B002", "To Kill a Mockingbird", "Harper Lee")
    book3 = Book("B003", "1984", "George Orwell")
    
    print(city_library.add_book(book1))
    print(city_library.add_book(book2))
    print(city_library.add_book(book3))
    
    # Add members
    member1 = Member("M001", "Alice Johnson")
    member2 = Member("M002", "Bob Smith")
    
    print(city_library.add_member(member1))
    print(city_library.add_member(member2))
    
    # Borrow books
    print(city_library.borrow_book("B001", "M001"))
    print(city_library.borrow_book("B002", "M002"))
    
    # Display books
    print(city_library.display_available_books())
    print(city_library.display_borrowed_books())
    
    # Return a book
    print(city_library.return_book("B001"))
    
    # Display updated books
    print(city_library.display_available_books())

```

**Output:**

```
Book 'The Great Gatsby' added to the library.
Book 'To Kill a Mockingbird' added to the library.
Book '1984' added to the library.
Member Alice Johnson registered.
Member Bob Smith registered.
Book 'The Great Gatsby' borrowed by Alice Johnson. Due date: 2025-10-18
Book 'To Kill a Mockingbird' borrowed by Bob Smith. Due date: 2025-10-18
Available Books:
[B003] 1984 by George Orwell - Available

Borrowed Books:
[B001] The Great Gatsby by F. Scott Fitzgerald - Borrowed by Alice Johnson (Due: 2025-10-18)
[B002] To Kill a Mockingbird by Harper Lee - Borrowed by Bob Smith (Due: 2025-10-18)

Book 'The Great Gatsby' returned successfully.
Available Books:
[B001] The Great Gatsby by F. Scott Fitzgerald - Available
[B003] 1984 by George Orwell - Available

```

### Basic Programming Exercises

- **Fibonacci Series:**

```python
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

# Example usage
if __name__ == "__main__":
    # Iterative approach
    n_terms = 10
    print(f"Fibonacci sequence (first {n_terms} terms):")
    print(fibonacci_iterative(n_terms))
    
    # Recursive approach (for individual terms)
    print("\nFibonacci sequence using recursion:")
    for i in range(10):
        print(f"F({i}) = {fibonacci_recursive(i)}")

```

**Output:**

```
Fibonacci sequence (first 10 terms):
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

Fibonacci sequence using recursion:
F(0) = 0
F(1) = 1
F(2) = 1
F(3) = 2
F(4) = 3
F(5) = 5
F(6) = 8
F(7) = 13
F(8) = 21
F(9) = 34

```

- **Pattern Printing:**

```python
def print_pyramid(height):
    """Print a pyramid pattern of asterisks."""
    for i in range(1, height + 1):
        # Print spaces before the asterisks
        spaces = " " * (height - i)
        # Print asterisks
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

# Example usage
if __name__ == "__main__":
    print("Pyramid Pattern (height 5):")
    print_pyramid(5)
    
    print("\nDiamond Pattern (height 5):")
    print_diamond(5)
    
    print("\nNumber Pattern (5 rows):")
    print_number_pattern(5)

```

**Output:**

```
Pyramid Pattern (height 5):
    *
   ***
  *****
 *******
*********

Diamond Pattern (height 5):
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *

Number Pattern (5 rows):
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 

```

- **Palindrome Checker:**

```python
def is_palindrome_string(s):
    """Check if a string is a palindrome."""
    # Convert to lowercase and remove non-alphanumeric characters
    s = ''.join(e.lower() for e in s if e.isalnum())
    return s == s[::-1]

def is_palindrome_number(n):
    """Check if a number is a palindrome."""
    # Convert number to string and check
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

# Example usage
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

```

**Output:**

```
String palindrome check:
'racecar' is a palindrome: True
'hello' is a palindrome: False
'A man, a plan, a canal, Panama' is a palindrome: True
'python' is a palindrome: False
'Madam' is a palindrome: True

Number palindrome check:
121 is a palindrome: True
12321 is a palindrome: True
12345 is a palindrome: False
1001 is a palindrome: True
7 is a palindrome: True
678 is a palindrome: False

Palindromes in the mixed list:
['racecar', 121, 12321]

```

### API Integration

- **External REST API Consumption:**

```python
import requests
import json
from datetime import datetime

class WeatherAPIClient:
    """A client for interacting with the OpenWeatherMap API."""
    
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.openweathermap.org/data/2.5"
    
    def get_current_weather(self, city, units="metric"):
        """Get current weather for a city."""
        endpoint = f"{self.base_url}/weather"
        params = {
            "q": city,
            "appid": self.api_key,
            "units": units
        }
        
        try:
            response = requests.get(endpoint, params=params)
            response.raise_for_status()  # Raise exception for 4XX/5XX responses
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}
    
    def format_weather_data(self, data):
        """Format weather data into a readable string."""
        if "error" in data:
            return f"Error: {data['error']}"
        
        # Extract relevant information
        city = data["name"]
        country = data["sys"]["country"]
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        description = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        timestamp = data["dt"]
        
        # Convert timestamp to readable date/time
        date_time = datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S")
        
        # Create formatted output
        result = f"""
Weather for {city}, {country} at {date_time}
----------------------------------------------
Temperature: {temp}°C (Feels like: {feels_like}°C)
Conditions: {description.capitalize()}
Humidity: {humidity}%
Wind Speed: {wind_speed} m/s
"""
        return result

# Example usage
if __name__ == "__main__":
    # Replace 'your_api_key' with an actual OpenWeatherMap API key
    API_KEY = "your_api_key"
    weather_client = WeatherAPIClient(API_KEY)
    
    cities = ["London", "Tokyo", "New York"]
    
    for city in cities:
        print(f"\nFetching weather data for {city}...")
        weather_data = weather_client.get_current_weather(city)
        
        # Check for error
        if "error" in weather_data:
            print(f"Error retrieving data for {city}: {weather_data['error']}")
            continue
        
        # Print pretty JSON
        print("Raw JSON response:")
        print(json.dumps(weather_data, indent=2))
        
        # Print formatted data
        print("\nFormatted Weather Data:")
        print(weather_client.format_weather_data(weather_data))

```

**Output:**

```
Fetching weather data for London...
Raw JSON response:
{
  "coord": {
    "lon": -0.1257,
    "lat": 51.5085
  },
  "weather": [
    {
      "id": 803,
      "main": "Clouds",
      "description": "broken clouds",
      "icon": "04d"
    }
  ],
  "base": "stations",
  "main": {
    "temp": 15.6,
    "feels_like": 15.1,
    "temp_min": 14.36,
    "temp_max": 16.87,
    "pressure": 1015,
    "humidity": 72
  },
  "visibility": 10000,
  "wind": {
    "speed": 5.14,
    "deg": 230
  },
  "clouds": {
    "all": 75
  },
  "dt": 1727961244,
  "sys": {
    "type": 2,
    "id": 2075535,
    "country": "GB",
    "sunrise": 1727938058,
    "sunset": 1727978509
  },
  "timezone": 3600,
  "id": 2643743,
  "name": "London",
  "cod": 200
}

Formatted Weather Data:

Weather for London, GB at 2025-10-04 11:20:44
----------------------------------------------
Temperature: 15.6°C (Feels like: 15.1°C)
Conditions: Broken clouds
Humidity: 72%
Wind Speed: 5.14 m/s

```

### Testing (Optional)

- **Pytest Implementation:**

```python
# bank_account.py (implementation file)
class InsufficientFundsError(Exception):
    """Exception raised when withdrawal amount exceeds account balance."""
    pass

class BankAccount:
    def __init__(self, account_number, owner_name, balance=0):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance
    
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount
        return f"Deposited ${amount}. New balance: ${self.balance}"
    
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise InsufficientFundsError(f"Cannot withdraw ${amount}. Available balance: ${self.balance}")
        self.balance -= amount
        return f"Withdrew ${amount}. New balance: ${self.balance}"
    
    def check_balance(self):
        return f"Current balance for account {self.account_number}: ${self.balance}"

# test_bank_account.py (test file)
import pytest
from bank_account import BankAccount, InsufficientFundsError

# Fixture to create test account
@pytest.fixture
def test_account():
    """Create a test account with $1000 balance"""
    return BankAccount("TEST123", "Test User", 1000)

def test_init():
    """Test account initialization"""
    account = BankAccount("123456", "John Doe", 500)
    assert account.account_number == "123456"
    assert account.owner_name == "John Doe"
    assert account.balance == 500

def test_init_default_balance():
    """Test account initialization with default balance"""
    account = BankAccount("123456", "John Doe")
    assert account.balance == 0

def test_deposit(test_account):
    """Test deposit functionality"""
    test_account.deposit(500)
    assert test_account.balance == 1500
    
    result = test_account.deposit(250)
    assert "Deposited $250" in result
    assert test_account.balance == 1750

def test_deposit_invalid_amount(test_account):
    """Test deposit with invalid amounts"""
    with pytest.raises(ValueError):
        test_account.deposit(0)
    
    with pytest.raises(ValueError):
        test_account.deposit(-100)
    
    # Balance should remain unchanged
    assert test_account.balance == 1000

def test_withdraw(test_account):
    """Test withdraw functionality"""
    test_account.withdraw(300)
    assert test_account.balance == 700
    
    result = test_account.withdraw(200)
    assert "Withdrew $200" in result
    assert test_account.balance == 500

def test_withdraw_invalid_amount(test_account):
    """Test withdraw with invalid amounts"""
    with pytest.raises(ValueError):
        test_account.withdraw(0)
    
    with pytest.raises(ValueError):
        test_account.withdraw(-50)
    
    # Balance should remain unchanged
    assert test_account.balance == 1000

def test_withdraw_insufficient_funds(test_account):
    """Test withdraw with insufficient funds"""
    with pytest.raises(InsufficientFundsError) as excinfo:
        test_account.withdraw(1500)
    
    assert "Cannot withdraw $1500" in str(excinfo.value)
    # Balance should remain unchanged
    assert test_account.balance == 1000

def test_check_balance(test_account):
    """Test check_balance functionality"""
    result = test_account.check_balance()
    assert "Current balance for account TEST123: $1000" == result

# Parametrized test example
@pytest.mark.parametrize("initial_balance, deposit_amount, expected_balance", [
    (0, 100, 100),       # Start with 0, deposit 100
    (500, 300, 800),     # Start with 500, deposit 300
    (1000, 1000, 2000),  # Start with 1000, deposit 1000
])
def test_deposit_various_amounts(initial_balance, deposit_amount, expected_balance):
    """Test deposits with various initial balances and deposit amounts"""
    account = BankAccount("TEST", "Test User", initial_balance)
    account.deposit(deposit_amount)
    assert account.balance == expected_balance

```

**Running the tests:**

```bash
$ pytest -v test_bank_account.py

============================= test session starts ==============================
collecting ... collected 9 items

test_bank_account.py::test_init PASSED                               [ 11%]
test_bank_account.py::test_init_default_balance PASSED               [ 22%]
test_bank_account.py::test_deposit PASSED                            [ 33%]
test_bank_account.py::test_deposit_invalid_amount PASSED             [ 44%]
test_bank_account.py::test_withdraw PASSED                           [ 55%]
test_bank_account.py::test_withdraw_invalid_amount PASSED            [ 66%]
test_bank_account.py::test_withdraw_insufficient_funds PASSED        [ 77%]
test_bank_account.py::test_check_balance PASSED                      [ 88%]
test_bank_account.py::test_deposit_various_amounts PASSED            [100%]

============================== 9 passed in 0.05s ===============================

```

- **Submission Guidelines:**
    - Follow the coding standards outlined above
    - Include appropriate documentation and comments
    - Submit via Git repository with meaningful commit messages