
print("=== FUNCTIONS: CREATING REUSABLE MATHEMATICAL TOOLS ===")


def greet_student(name):
    return f"Hello, {name}! Welcome to math class."


print(greet_student("Alice"))


def calculate_area(length, width):
    return length * width

print(f"Area of 10x5 rectangle: {calculate_area(10,5)} square units")


def power_function(base, exponent=2):
    return base ** exponent

print(f"5² = {power_function(5)}")
print(f"5³ = {power_function(5,3)}")

def linear_function(x, slope, intercept):
  return slope * x + intercept

print("Linear y=2x+1, x=3:", linear_function(3,2,1))

