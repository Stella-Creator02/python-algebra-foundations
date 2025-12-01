
# 02_functions/function_syntax.py

print("=== FUNCTIONS: CREATING REUSABLE MATHEMATICAL TOOLS ===")

def greet_student(name):
    return f"Hello, {name}! Welcome to math class."

def calculate_area(length, width):
    return length * width

def linear_function(x, slope, intercept):
    return slope*x + intercept

def power_function(base, exponent=2):
    return base ** exponent

# Test the functions
print(greet_student("Alice"))
print("Area 10x5:", calculate_area(10,5))
print("Linear y=2x+1, x=3:", linear_function(3,2,1))
print("Power 5^2 and 5^3:", power_function(5), power_function(5,3))
