def find_common_divisors(num1, num2):
    # Find the minimum of the two numbers
    min_num = min(num1, num2)

    # Initialize a list to store common divisors
    common_divisors = []

    # Iterate from 1 to min_num
    for i in range(1, min_num + 1):
        # Check if i is a divisor of both numbers
        if num1 % i == 0 and num2 % i == 0:
            common_divisors.append(i)

    return common_divisors


# Example usage:
number1 = 36
number2 = 48

result = find_common_divisors(number1, number2)

print(f"Common divisors between {number1} and {number2}:{result}")


