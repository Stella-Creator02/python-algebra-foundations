
print("=== 20 ALGEBRAIC FUNCTION CHALLENGES ===")


def welcome_student(name):
    return f"Hello, {name}! Welcome to math class."


def perimeter_of_square(side_length):
    return 4 * side_length


def area_of_circle(radius):
    return 3.14 * radius ** 2


def area_of_triangle(base, height):
    return 0.5 * base * height


def find_hypotenuse(a, b):
    return (a**2 + b**2) ** 0.5


def calculate_simple_interest(principal, rate, time):
    return principal * rate * time


def average_of_three(a, b, c):
    return (a + b + c) / 3


def find_max(num1, num2):
    return num1 if num1 > num2 else num2


def calculate_power(base, exponent):
    return base ** exponent


def simplify_fraction(numerator, denominator):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    common = gcd(numerator, denominator)
    return numerator // common, denominator // common


def celsius_to_fahrenheit(c_temp):
    return (c_temp * 9/5) + 32


def feet_to_meters(feet):
    return feet * 0.3048


def find_percentage(part, whole):
    return (part / whole) * 100


def find_slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)


def find_distance(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5


def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return "No real roots"
    root1 = (-b + discriminant**0.5) / (2*a)
    root2 = (-b - discriminant**0.5) / (2*a)
    return root1, root2


def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


def is_even(number):
    return number % 2 == 0


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            return False
    return True


def is_solution(x, y, eq1, eq2):
    a1, b1, c1 = eq1
    a2, b2, c2 = eq2
    return abs(a1*x + b1*y - c1) < 1e-6 and abs(a2*x + b2*y - c2) < 1e-6

# --- Test all challenges ---
if __name__ == "__main__":
    print("1.", welcome_student("Alice"))
    print("2. Perimeter of square 5:", perimeter_of_square(5))
    print("3. Area of circle radius 7:", area_of_circle(7))
    print("4. Area of triangle 10x5:", area_of_triangle(10,5))
    print("5. Hypotenuse 3-4-5:", find_hypotenuse(3,4))
    print("6. Simple interest $1000, 5%, 2 yrs:", calculate_simple_interest(1000,0.05,2))
    print("7. Average 10,20,30:", average_of_three(10,20,30))
    print("8. Max of 15,25:", find_max(15,25))
    print("9. 2^8:", calculate_power(2,8))
    print("10. Simplify 8/12:", simplify_fraction(8,12))
    print("11. 25°C to F:", celsius_to_fahrenheit(25))
    print("12. 10 ft to m:", feet_to_meters(10))
    print("13. 25/50 %:", find_percentage(25,50))
    print("14. Slope (1,2) to (4,8):", find_slope(1,2,4,8))
    print("15. Distance (1,1) to (4,5):", find_distance(1,1,4,5))
    print("16. Quadratic x²-5x+6:", solve_quadratic(1,-5,6))
    print("17. Factorial 5:", factorial(5))
    print("18. Is 7 even?", is_even(7))
    print("19. Is 17 prime?", is_prime(17))
    equation1 = (2,3,12)
    equation2 = (1,-1,1)
    print("20. Is (3,2) solution?", is_solution(3,2,equation1,equation2))
    print("\n🎉 ALL 20 CHALLENGES COMPLETED! 🎉")
