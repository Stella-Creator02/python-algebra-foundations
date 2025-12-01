

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
numbers = [7, 12, -3]
for n in numbers:
    print(f"\nAnalyzing number: {n}")
    if n > 0:
        print("  - Positive number")
    elif n < 0:
        print("  - Negative number")
    if n % 2 == 0:
        print("  - Even number")
    else:
        print("  - Odd number")
   
    is_prime = True
    if n < 2:
        is_prime = False
    else:
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                is_prime = False
                break
    if n >= 2:
        if is_prime:
            print("  - Prime number")
        else:
            print("  - Composite number")


print("\n--- 4. Practical Algebra: Summation ---")
sum_loop = sum(range(1, 11))
sum_formula = 10*(10+1)//2
print(f"Sum of first 10 numbers using loop: {sum_loop}")
print(f"Sum of first 10 numbers using formula: {sum_formula}")
print(f"Match: {sum_loop == sum_formula}")


print("\n--- 5. Break and Continue - Loop Control ---")

n = 21
while True:
    is_prime = True
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f"First prime > 20: {n}")
        break
    n += 1


print("\nEven numbers from 1 to 10 (using continue):")
for i in range(1, 11):
    if i % 2 != 0:
        continue
    print(i)

print("\n✅ Control flow basics complete! Ready for advanced algorithms.")
