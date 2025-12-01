
print("=== CONTROL FLOW: LOOPS AND LOGIC FOR ALGEBRA ===")


print("\n--- 1. For Loops - Repeating Operations ---")
for i in range(1, 6):
    print(f"  Number: {i}")

print("\nFirst 5 square numbers:")
for i in range(1, 6):
    print(f"  {i}² = {i**2}")

print("\n--- 2. While Loops - Conditional Repetition ---")
countdown = 5
print("Countdown from 5:")
while countdown > 0:
    print(f"  {countdown}...")
    countdown -= 1
print("  Blastoff! 🚀")


print("\n--- 3. Conditional Logic - Mathematical Decisions ---")
def check_number_properties(number):
    print(f"\nAnalyzing number: {number}")
    if number > 0:
        print("  - Positive number")
    elif number < 0:
        print("  - Negative number")
    else:
        print("  - Zero")

    if number % 2 == 0:
        print("  - Even number")
    else:
        print("  - Odd number")

    if number > 1:
        is_prime = True
        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                is_prime = False
                break
        if is_prime:
            print("  - Prime number")
        else:
            print("  - Composite number")

check_number_properties(7)
check_number_properties(12)
check_number_properties(-3)


print("\n--- 4. Practical Algebra: Summation ---")
def sum_first_n_numbers(n):
    return sum(range(1, n+1))

n = 10
loop_sum = sum_first_n_numbers(n)
formula_sum = n * (n + 1) // 2

print(f"Sum of first {n} numbers:")
print(f"  Using loop: {loop_sum}")
print(f"  Using formula: {formula_sum}")
print(f"  Match: {loop_sum == formula_sum}")


print("\n--- 5. Break and Continue - Loop Control ---")


number = 21
while True:
    is_prime = True
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f"First prime > 20: {number}")
        break
    number += 1


print("\nEven numbers from 1 to 10 (using continue):")
for i in range(1, 11):
    if i % 2 != 0:
        continue
    print(f"  {i}")

print("\n✅ Control flow basics complete! Ready for advanced algorithms.")
