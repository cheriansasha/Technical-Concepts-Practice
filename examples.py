# Try-Catch Blocks example → differentiate between that and exceptions
print("Try-Catch Block example: ")
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
    
# Exceptions are errors that occur during code execution. Try-catch blocks are the syntax used 
# to catch and handle those exceptions, preventing program crashes.

print("----------------------------------------------\n")

# Try-catch-finally block example:
# exception is caught:
print("Try-Catch-Finally Block example (exception IS caught): ")

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("Always runs\n")
    
# exception is not caught:
print("Try-Catch-Finally Block example (exception IS NOT caught): ")

try:
    result = 10 / 5
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("Always runs")  
    
print("----------------------------------------------\n")

# Try-catch-finally block with custom exception example:
print("Try-Catch-Finally Block with custom exception example: ")
class InvalidAge(Exception):
    pass

def check_age(age):
    if age < 0:
        raise InvalidAge()

try:
    check_age(-5)
except InvalidAge:
    print("Age cannot be negative")
finally:
    print("Always runs")
    
print("----------------------------------------------\n")

# Try-catch-finally block with real-world use case of finally block (closing a file)
print("Try-Catch-Finally Block with real-world use case of finally block (closing a file): ")

# Create the file first
with open("data.txt", "w") as f:
    f.write("Hello, World!")

# Now use it in try-catch-finally
try:
    file = open("data.txt", "r")
    result = 10 / 0  # ZeroDivisionError
except ZeroDivisionError:
    print("Division by zero error")
finally:
    print("Closing the file after ZeroDivisionError exception was raised")
    file.close()
    
print("----------------------------------------------\n")
print("Recursion → being able to print out a string using recursion: ")

def print_string_forward(text):
    # base case
    if len(text) == 0:
        return
    
    # Make recursive call with everything except the last character
    print_string_forward(text[:-1])
    
    # Print the last character after recursion returns
    print(text[-1], end=' ')

# This prints "Hello!" in correct order
print_string_forward("Sasha")

print("\n----------------------------------------------\n")

