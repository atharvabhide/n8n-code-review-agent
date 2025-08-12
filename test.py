# This is a comment in Python.
# It explains what the code does but is ignored by the interpreter.

# Print a simple message to the console
print("Hello, World!")

# Define a function that takes a name as an argument and prints a greeting
def greet(name):
    """
    This function takes a name (string) as input
    and prints a personalized greeting.
    """
    print(f"Hello, {name}! Welcome to Python.")

# Call the greet function with a specific name
greet("Alice")

# You can also use input() to get user input
user_name = input("Enter your name: ")
greet(user_name)
