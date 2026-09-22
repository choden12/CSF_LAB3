import random
import time


# ==========================================
# TRADITIONAL MULTIPLICATION
# O(n^2)
# ==========================================

def traditional_multiply(num1, num2):

    # Convert each digit into an integer
    a = [int(digit) for digit in num1]
    b = [int(digit) for digit in num2]

    # Create result array
    result = [0] * (len(a) + len(b))

    # Multiply digit by digit
    for i in range(len(a) - 1, -1, -1):

        for j in range(len(b) - 1, -1, -1):

            product = a[i] * b[j]

            position = i + j + 1

            result[position] += product

            # Handle carry
            result[position - 1] += result[position] // 10
            result[position] %= 10

    # Convert result to string
    result_string = ''.join(str(digit) for digit in result)

    # Remove leading zeros
    result_string = result_string.lstrip('0')

    if result_string == '':
        result_string = '0'

    return result_string


# ==========================================
# STRING ADDITION
# ==========================================

def add_strings(a, b):

    i = len(a) - 1
    j = len(b) - 1
    carry = 0

    result = []

    while i >= 0 or j >= 0 or carry:

        digit_a = int(a[i]) if i >= 0 else 0
        digit_b = int(b[j]) if j >= 0 else 0

        total = digit_a + digit_b + carry

        result.append(str(total % 10))

        carry = total // 10

        i -= 1
        j -= 1

    return ''.join(result[::-1])


# ==========================================
# STRING SUBTRACTION
# Assumes a >= b
# ==========================================

def subtract_strings(a, b):

    i = len(a) - 1
    j = len(b) - 1

    borrow = 0
    result = []

    while i >= 0:

        digit_a = int(a[i]) - borrow

        digit_b = int(b[j]) if j >= 0 else 0

        if digit_a < digit_b:

            digit_a += 10
            borrow = 1

        else:

            borrow = 0

        result.append(str(digit_a - digit_b))

        i -= 1
        j -= 1

    # Reverse result
    result = ''.join(result[::-1])

    # Remove leading zeros
    result = result.lstrip('0')

    if result == '':
        result = '0'

    return result


# ==========================================
# KARATSUBA MULTIPLICATION
# O(n^1.585)
# ==========================================

def karatsuba(num1, num2):

    # Remove leading zeros
    num1 = num1.lstrip('0') or '0'
    num2 = num2.lstrip('0') or '0'

    # Base case
    if len(num1) == 1 and len(num2) == 1:

        result = int(num1) * int(num2)

        return str(result)

    # Make both numbers the same length
    n = max(len(num1), len(num2))

    num1 = num1.zfill(n)
    num2 = num2.zfill(n)

    # Make length even
    if n % 2 != 0:

        n += 1

        num1 = num1.zfill(n)
        num2 = num2.zfill(n)

    # Split position
    m = n // 2

    # Split first number
    high1 = num1[:m]
    low1 = num1[m:]

    # Split second number
    high2 = num2[:m]
    low2 = num2[m:]

    # --------------------------------------
    # Three recursive multiplications
    # --------------------------------------

    z2 = karatsuba(high1, high2)

    z0 = karatsuba(low1, low2)

    sum1 = add_strings(high1, low1)
    sum2 = add_strings(high2, low2)

    z1 = karatsuba(sum1, sum2)

    # z1 = z1 - z2 - z0
    z1 = subtract_strings(z1, z2)

    z1 = subtract_strings(z1, z0)

    # --------------------------------------
    # Combine the three results
    # --------------------------------------

    part1 = z2 + "0" * (2 * (n - m))

    part2 = z1 + "0" * (n - m)

    result = add_strings(part1, part2)

    result = add_strings(result, z0)

    return result.lstrip('0') or '0'


# ==========================================
# GENERATE RANDOM NUMBER
# ==========================================

def generate_number(digits):

    # First digit cannot be zero
    first_digit = str(random.randint(1, 9))

    # Generate remaining digits
    remaining_digits = ''.join(
        str(random.randint(0, 9))
        for _ in range(digits - 1)
    )

    return first_digit + remaining_digits


# ==========================================
# SMALL TEST
# ==========================================

print("==========================================")
print("Small Test")
print("==========================================")

num1 = "123"
num2 = "456"

traditional_result = traditional_multiply(num1, num2)

karatsuba_result = karatsuba(num1, num2)

print("Number 1:", num1)
print("Number 2:", num2)

print("Traditional Result:", traditional_result)

print("Karatsuba Result:", karatsuba_result)

print("Results Match:", traditional_result == karatsuba_result)


# ==========================================
# PERFORMANCE TESTING
# ==========================================

print()
print("==========================================")
print("Performance Testing")
print("==========================================")

sizes = [8, 16, 32, 64, 128, 256, 512, 1024]

for size in sizes:

    # Generate two random numbers
    num1 = generate_number(size)
    num2 = generate_number(size)

    # --------------------------------------
    # Traditional multiplication
    # --------------------------------------

    start = time.perf_counter()

    traditional_result = traditional_multiply(num1, num2)

    traditional_time = time.perf_counter() - start

    # --------------------------------------
    # Karatsuba multiplication
    # --------------------------------------

    start = time.perf_counter()

    karatsuba_result = karatsuba(num1, num2)

    karatsuba_time = time.perf_counter() - start

    # --------------------------------------
    # Verify results
    # --------------------------------------

    match = traditional_result == karatsuba_result

    # --------------------------------------
    # Display results
    # --------------------------------------

    print()
    print("Digits:", size)

    print("Traditional Time:",
          f"{traditional_time:.8f}",
          "seconds")

    print("Karatsuba Time:",
          f"{karatsuba_time:.8f}",
          "seconds")

    print("Results Match:", match)


# ==========================================
# END
# ==========================================

print()
print("==========================================")
print("Testing Completed")
print("==========================================")